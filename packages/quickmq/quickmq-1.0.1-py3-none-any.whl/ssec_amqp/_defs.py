"""
ssec_amqp._defs
~~~~~~~~~~~~~~~

Definitions that are used in ssec_amqp.
"""

# Inspired by the AMQP URI format, and adds the exchange to the end
AMQP_EXCHANGE_ID_FORMAT = "amqp://{user:s}@{host:s}:{port:d}{vhost:s}/{exchange:s}"

# Default AmqpExchange values
DEFAULT_USER = "guest"
DEFAULT_PASS = "guest"
DEFAULT_PORT = 5672
DEFAULT_VHOST = "/"
DEFAULT_EXCHANGE = ""

# Default AmqpClient values
DEFAULT_RECONNECT_WINDOW = -1
