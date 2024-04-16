import pytest

import ssec_amqp as mq
from ssec_amqp._defs import DEFAULT_RECONNECT_WINDOW


def is_reconnecting(client: mq.AmqpClient, exchange: mq.AmqpExchange) -> bool:
    return client.connections.get(exchange.id) == "reconnecting"


def is_connected(client: mq.AmqpClient, exchange: mq.AmqpExchange) -> bool:
    return client.connections.get(exchange.id) == "connected"


@pytest.fixture(scope="function")
def mock_exchange(mocker):
    exh = mq.AmqpExchange("test")
    mock_exchange = mocker.MagicMock(wraps=exh, name="MockExchange")
    yield mock_exchange


def test_init():
    cl = mq.AmqpClient()
    assert cl.connections == {}
    assert cl.reconnect_window == DEFAULT_RECONNECT_WINDOW

    new_window = 20
    cl = mq.AmqpClient(new_window)
    assert cl.connections == {}
    assert cl.reconnect_window == new_window


def test_connect_one(mocker):
    mock_exchange = mocker.MagicMock(set_spec=mq.AmqpExchange, name="MockExchange")
    mock_exchange_connected = mocker.PropertyMock(return_value=False)
    mock_exchange.connect.return_value = None
    type(mock_exchange).connected = mock_exchange_connected

    cl = mq.AmqpClient()
    cl.connect(mock_exchange)
    mock_exchange_connected.return_value = True

    assert mock_exchange.connect.call_count == 1
    assert is_connected(cl, mock_exchange)
