from typing import Any, Optional
import pytest

from pika.exceptions import AMQPConnectionError

from ssec_amqp._utils import catch_amqp_errors


def mock_function(
    to_return: Optional[Any] = None, to_raise: Optional[Exception] = None
):
    if to_return is not None:
        return to_return
    if to_raise is not None:
        raise to_raise
    return None


def test_catch_amqp_errors_no_error():
    rv = 5
    assert catch_amqp_errors(mock_function)(to_return=rv) == rv


def test_catch_amqp_errors_amqp_error():
    with pytest.raises(ConnectionError):
        catch_amqp_errors(mock_function)(to_raise=AMQPConnectionError)


def test_catch_amqp_errors_diff_error():
    err = TypeError
    with pytest.raises(err):
        catch_amqp_errors(mock_function)(to_raise=err)
