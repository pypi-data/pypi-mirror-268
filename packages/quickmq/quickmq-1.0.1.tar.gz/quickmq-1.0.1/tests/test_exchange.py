from typing import Hashable
from unittest.mock import DEFAULT

import pika
from pika.exceptions import AMQPConnectionError
import pytest

from ssec_amqp import (
    AmqpExchange,
    DEFAULT_EXCHANGE,
    DEFAULT_PORT,
    DEFAULT_VHOST,
)


def test_initialization():
    test_dest = "amqp"
    test_user = "u"
    test_pass = "p"
    test_port = 123
    test_vhost = "/new"
    test_exch = "model"

    ex = AmqpExchange(test_dest, test_user, test_pass)

    assert not ex.connected
    assert ex.host == test_dest
    assert ex.user == test_user
    assert ex.port == DEFAULT_PORT
    assert ex.exchange == DEFAULT_EXCHANGE
    assert ex.vhost == DEFAULT_VHOST

    ex1 = AmqpExchange(
        test_dest, test_user, test_pass, test_exch, test_vhost, test_port
    )

    assert ex1.port == test_port
    assert ex1.vhost == test_vhost
    assert ex1.exchange == test_exch


def test_connect(mocker):
    mocker.patch(
        "pika.BlockingConnection",
        autospec=True,
        create=True,
        side_effect=(AMQPConnectionError, DEFAULT),
    )

    ex = AmqpExchange("localhost", "guest", "guest")

    with pytest.raises(ConnectionError):
        ex.connect()

    pika.BlockingConnection.assert_called()
    assert not ex.connected

    ex.connect()
    pika.BlockingConnection.assert_called()
    assert ex.connected


@pytest.mark.parametrize(
    ["con1", "con2"],
    [
        (("host",), ("host",)),
        (("host1",), ("host2",)),
        (("host", "user"), ("host", "user")),
        (
            (
                "host",
                "user1",
            ),
            ("host", "user2"),
        ),
        (("host", "user", "pass"), ("host", "user", "pass")),
        (("host", "user", "pass1"), ("host", "user", "pass2")),
        (("host", "user", "pass", "exch"), ("host", "user", "pass", "exch")),
        (("host", "user", "pass", "exch1"), ("host", "user", "pass", "exch2")),
        (
            ("host", "user", "pass", "exch", "vhost"),
            ("host", "user", "pass", "exch", "vhost"),
        ),
        (
            ("host", "user", "pass", "exch", "vhost1"),
            ("host", "user", "pass", "exch", "vhost2"),
        ),
        (
            ("host", "user", "pass", "exch", "vhost", 4000),
            ("host", "user", "pass", "exch", "vhost", 4000),
        ),
        (
            ("host", "user", "pass", "exch", "vhost", 4001),
            ("host", "user", "pass", "exch", "vhost", 4002),
        ),
    ],
)
def test_equality(con1, con2):
    ex1 = AmqpExchange(*con1)
    ex2 = AmqpExchange(*con2)
    assert ex1 != con1
    assert ex2 != con2
    if con1 == con2:
        assert ex1 == ex2
        assert ex1.id == ex2.id
    elif con1[:2] == con2[:2] and con1[3:] == con2[3:]:
        # password doesn't get checked for equality!
        assert ex1 == ex2
        assert ex1.id == ex2.id
    else:
        assert ex1 != ex2
        assert ex1.id != ex2.id


def test_hashable():
    assert isinstance(AmqpExchange, Hashable)
    ex1 = AmqpExchange("test")
    ex2 = AmqpExchange("test")
    ex3 = AmqpExchange("nottest")
    assert hash(ex1) == hash(ex2)
    assert hash(ex2) != hash(ex3)


def test_produce_not_connected():
    ex = AmqpExchange("test")
    with pytest.raises(RuntimeError):
        ex.produce("hello")


@pytest.mark.skip
def test_close(mocker):
    ex = AmqpExchange("test")
    mock_con = mocker.patch(ex, "_AmqpExchange__conn", create=False)
    assert mock_con.call_count == 0

    ex.close()
    assert mock_con.close.call_count == 0

    ex.connect()
    assert mock_con.call_count == 1

    ex.close()
    assert mock_con.close.call_count == 1
