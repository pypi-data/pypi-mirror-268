import json
from enum import Enum
import logging
from typing import Dict, List, Optional

import amqp
from amqp.exceptions import MessageNacked

from ._utils import RetryInterval, catch_amqp_errors, NOTYET
from ._defs import (
    AMQP_EXCHANGE_ID_FORMAT,
    DEFAULT_EXCHANGE,
    DEFAULT_PASS,
    DEFAULT_PORT,
    DEFAULT_USER,
    DEFAULT_VHOST,
    DEFAULT_RECONNECT_WINDOW,
)

LOG = logging.getLogger("ssec_amqp")


class DeliveryStatus(Enum):
    """Enum for status of messages being delivered"""

    # Message was acknowledged by the server.
    DELIVERED = "delivered"
    # Message was dropped due to reconnection.
    DROPPED = "dropped"
    # Message was rejected by the server.
    REJECTED = "rejected"


class AmqpExchange:
    """Abstraction of an exchange on a AMQP server."""

    def __init__(
        self,
        host: str,
        user: Optional[str] = None,
        password: Optional[str] = None,
        exchange: Optional[str] = None,
        vhost: Optional[str] = None,
        port: Optional[int] = None,
    ) -> None:
        """Initialize the AmqpExchange.

        Args:
            host (str): where the exchange is
            user (str): user to connect with
            password (str): password to connect with
            exchange (Optional[str], optional): name of the exchange. Defaults to None.
            vhost (Optional[str], optional): vhost of the exchange. Defaults to None.
            port (Optional[int], optional): port to connect with. Defaults to None.
        """
        self.host = host
        self.user = user or DEFAULT_USER
        self.vhost = vhost or DEFAULT_VHOST
        self.port = port or DEFAULT_PORT
        self.exchange = exchange or DEFAULT_EXCHANGE
        self.__password = password or DEFAULT_PASS

        self.__conn = None
        self.__chan = None
        self.__chan_id = None

    @property
    def connected(self) -> bool:
        return self.__conn is not None and self.__conn.connected

    @property
    def id(self) -> str:
        return str(self)

    @catch_amqp_errors
    def connect(self) -> None:
        """Connects the object to the AMQP exchange using the parameters supplied in constructor."""
        if self.connected:
            self.refresh()
            return

        self.__conn = amqp.Connection(
            f"{self.host}:{self.port}",
            userid=self.user,
            password=self.__password,
            confirm_publish=True,
        )
        self.__conn.connect()
        self.__chan = self.__conn.channel(channel_id=self.__chan_id)
        self.__chan_id = self.__chan.channel_id

    @catch_amqp_errors
    def produce(self, content_dict, route_key: Optional[str] = None) -> bool:
        """Produce a message to the exchange

        Args:
            content_dict (JSON): The body of the message to produce.
            key (Optional[str], optional): key to send with. Defaults to None.

        Raises:
            RuntimeError: If the AmqpExchange is not connected.
            ConnectionError: If there is a problem with the connection when publishing.

        Returns:
            bool: Was the message delivered?
        """
        self.refresh()
        content_json = json.dumps(content_dict)
        route_key = route_key or ""
        try:
            self.__chan.basic_publish(
                msg=amqp.Message(
                    body=content_json,
                    content_type="application/json",
                    content_encoding="utf-8",
                ),
                exchange=self.exchange,
                routing_key=route_key,
            )
            return True
        except MessageNacked:
            LOG.debug(f"{self} message was not delivered!")
            return False
        finally:
            if self.__conn.connected and self.__chan is None or not self.__chan.is_open:
                self.__chan = self.__conn.channel(channel_id=self.__chan_id)

    @catch_amqp_errors
    def refresh(self) -> None:
        """Refresh the AMQP connection, assure that it is still connected."""
        if self.__conn is None:
            raise RuntimeError(
                f"Must call connect() before performing this action on{self!r}!"
            )
        try:
            self.__conn.heartbeat_tick()
        except amqp.ConnectionForced:
            self.connect()  # Try again on heartbeat misses

    def close(self) -> None:
        """Closes the connection to the AMQP exchange."""
        if self.__conn is None:
            return
        self.__conn.collect()

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return AMQP_EXCHANGE_ID_FORMAT.format(
            user=self.user,
            host=self.host,
            port=self.port,
            vhost=self.vhost,
            exchange=self.exchange,
        )

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, self.__class__):
            return False
        return (
            __value.host == self.host
            and __value.exchange == self.exchange
            and __value.user == self.user
            and __value.port == self.port
            and __value.vhost == self.vhost
        )


# TODO: What to do when exchange disconnects?
class AmqpClient:
    """Client that manages multiple AmqpExchanges at once."""

    def __init__(self, reconnect_window: Optional[float] = None) -> None:
        """Initialize a AmqpClient.

        Args:
            reconnect_window (Optional[float], optional): How long an AmqpExchange
            has to reconnect before an error is raised. Negative for infinite time.
            Defaults to -1.
        """
        self.reconnect_window = reconnect_window or DEFAULT_RECONNECT_WINDOW

        self._connected_pool: List[AmqpExchange] = []
        self._reconnect_pool: Dict[AmqpExchange, RetryInterval] = {}

    @property
    def connections(self) -> Dict[str, str]:
        self._refresh_pools()
        d = {exch.id: "connected" for exch in self._connected_pool}
        d.update({exch.id: "reconnecting" for exch in self._reconnect_pool})
        return d

    def connect(self, exchange: AmqpExchange) -> None:
        """Connect this AmqpClient to an AmqpExchange

        Args:
            exchange (AmqpExchange): The AmqpExchange to connect to.

        Raises:
            ConnectionError: If it cannot connect to the exchange.
        """
        self._refresh_pools()  # Could raise a timeout error!
        LOG.debug(f"Attempting to connect to {exchange}")

        if exchange in self._connected_pool:
            LOG.debug(f"Already connected to {exchange}, skipping...")
            return

        if exchange in self._reconnect_pool or not exchange.connected:
            exchange.connect()

        LOG.debug(f"Successfully connected to {exchange}")
        self._to_connected(exchange)

    def publish(
        self, message, route_key: Optional[str] = None
    ) -> Dict[str, DeliveryStatus]:
        """Publish an AMQP message to all exchanges connected to this client.

        Args:
            message (JSONable): A JSON-able message to publish
            route_key (Optional[str], optional): the route key to publish with. Defaults to None.

        Returns:
            Dict[str, DeliveryStatus]: The status of the publish to all exchanges connected to this client.
        """
        status = {}
        self._refresh_pools()
        for exchange in self._connected_pool:
            try:
                routable = exchange.produce(message, route_key)
            except ConnectionError:
                self._to_reconnect(exchange)
            else:
                status[exchange.id] = (
                    DeliveryStatus.DELIVERED if routable else DeliveryStatus.REJECTED
                )

        # Set status as dropped for all reconnecting exchanges
        status.update(
            {exchange.id: DeliveryStatus.DROPPED for exchange in self._reconnect_pool}
        )
        return status

    def disconnect(self, exchange: Optional[AmqpExchange] = None) -> None:
        """Disconnect this AmqpClient from one or all exchanges.

        Args:
            exchange (Optional[AmqpExchange], optional): A specific exchange to disconnect from.
            If none, disconnect from all exchanges. Defaults to None.
        """
        if exchange is not None:
            exchange.close()
            self._reconnect_pool.pop(exchange, None)
            try:
                self._connected_pool.remove(exchange)
            except ValueError:
                pass
            return

        for exchange in self._connected_pool:
            exchange.close()
        for exchange in self._reconnect_pool:
            exchange.close()
        self._reconnect_pool.clear()
        self._connected_pool.clear()

    def _to_reconnect(self, exchange: AmqpExchange) -> None:
        """Move an exchange to reconnecting pool.

        Args:
            exchange (AmqpExchange): AmqpExchange to move.
        """
        if exchange in self._connected_pool:
            self._connected_pool.remove(exchange)
        LOG.info(f"Moving {exchange!r} to reconnect dict")
        self._reconnect_pool[exchange] = RetryInterval(
            exchange.connect,
            self.reconnect_window,
            (ConnectionError,),
        )

    def _to_connected(self, exchange: AmqpExchange) -> None:
        """Move an exchange to connected pool.

        Args:
            exchange (AmqpExchange): AmqpExchange to move.
        """
        if exchange in self._reconnect_pool:
            del self._reconnect_pool[exchange]
        LOG.info(f"Moving {exchange!r} to connected list")
        self._connected_pool.append(exchange)

    def _refresh_pools(self) -> None:
        """Refresh this client's pools. Checks if exchanges can reconnect."""
        LOG.debug("Refreshing reconnect pool")
        for exchange, reconnect in self._reconnect_pool.copy().items():
            if reconnect() is NOTYET:
                LOG.debug(f"{exchange} not yet ready to reconnect")
            else:
                LOG.debug(f"Moving {exchange!r} to be connected")
                self._to_connected(exchange)
        for exchange in self._connected_pool:
            try:
                exchange.refresh()
            except ConnectionError:
                LOG.debug(f"{exchange} is not connected!")
                self._to_reconnect(exchange)
