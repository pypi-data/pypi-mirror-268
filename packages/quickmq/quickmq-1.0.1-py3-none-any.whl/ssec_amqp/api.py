"""
ssec_amqp.api
~~~~~~~~~~~~~

A public facing api to easily use AmqpClient. Not best coding practice,
but is useful for users at the SSEC.
"""

import atexit
from typing import Dict, Optional

from . import AmqpClient, AmqpExchange, DeliveryStatus

__CLIENT = AmqpClient()

atexit.register(__CLIENT.disconnect)


def configure(
    reconnect_window: Optional[float] = None,
) -> None:
    """Configure the current client.

    Args:
        reconnect_window (Optional[float], optional): How long to wait until a reconnecting exchange will throw an error. Defaults to None.
    """
    __CLIENT.reconnect_window = reconnect_window


def connect(
    host: str,
    *hosts: str,
    user: Optional[str] = None,
    password: Optional[str] = None,
    exchange: Optional[str] = None,
    port: Optional[int] = None,
    vhost: Optional[str] = None,
) -> None:
    """Connect to one or more AMQP exchanges.

    Args:
        host (str): hostname of server to connect to.
        user (Optional[str], optional): User to connect with. Defaults to None.
        password (Optional[str], optional): Password to connect with. Defaults to None.
        exchange (Optional[str], optional): Exchange to connect to. Defaults to None.
        port (Optional[int], optional): Port to connect to. Defaults to None.
        vhost (Optional[str], optional): Vhost to connect to. Defaults to None.
    """
    exchanges = [
        AmqpExchange(dest, user, password, exchange, vhost, port)
        for dest in (host,) + hosts
    ]
    for exch in exchanges:
        exch.connect()
    for exch in exchanges:
        __CLIENT.connect(exch)


def status() -> Dict[str, str]:
    """Get the status of all current connections.

    Returns:
        Dict[str, str]: A dictionary containing all of the current connections and there status: either 'connected' or 'reconnecting'.
    """
    return __CLIENT.connections


def publish(message, route_key: Optional[str] = None) -> Dict[str, DeliveryStatus]:
    """Publish a message to all currently connected AMQP exchanges.

    Args:
        message (Any): The message to publish, must be json-able.
        route_key (Optional[str], optional): The key to publish the message with. Defaults to None.

    Raises:
        RuntimeError: If not connected to any AMQP exchanges currently.

    Returns:
        Dict[str, DeliveryStatus]: The delivery status to all of the currently connected AMQP exchanges.
    """
    if not __CLIENT.connections:
        raise RuntimeError("Not connected to any exchange(s)!")
    return __CLIENT.publish(message, route_key=route_key)


def disconnect():
    """Disconnect from all AMQP exchanges."""
    __CLIENT.disconnect()
