"""
ssec_amqp._utils
~~~~~~~~~~~~~~~~

Internal utility classes/functions.
"""

import time

from amqp import Connection


class NotYet(object):
    """Sentinal class for when a retry is not yet ready"""

    pass


# Sentinal to use for RetryInterval
NOTYET = NotYet()


class RetryInterval:
    def __init__(self, action, total_interval: float, errors=(Exception)) -> None:
        self._init_time = time.time()

        self.action = action
        self.errors = errors

        if total_interval < 0:
            self._max_time = float("inf")
        else:
            self._max_time = self._init_time + total_interval

    def __call__(self) -> NotYet:
        cur_time = time.time()

        try:
            return self.action()
        except self.errors as e:
            if cur_time >= self._max_time:
                raise TimeoutError(
                    f"Action {self.action!r} could not complete on time!"
                ) from e
            return NOTYET


def catch_amqp_errors(func):
    """Utility decorator to catch all of Pika's AMQPConnectionError and
    raise them as built-in ConnectionError

    Args:
        func (Callable): Function to decorate
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Connection.recoverable_connection_errors as e:
            raise ConnectionError("AMQP Connection Error") from e

    return wrapper
