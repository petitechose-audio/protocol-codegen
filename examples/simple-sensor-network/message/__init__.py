# Import all messages to make them available to protocol generator
from .sensor import *
from .network import *

# All messages list for generator
ALL_MESSAGES = [
    # Sensor messages
    SENSOR_READING_SINGLE,
    SENSOR_READING_BATCH,
    REQUEST_SENSOR_LIST,
    SENSOR_LIST,
    SENSOR_CONFIG_SET,
    SENSOR_CONFIG_GET,
    SENSOR_ACTIVATE,
    SENSOR_DEACTIVATE,

    # Network messages
    NETWORK_STATUS,
    REQUEST_NETWORK_STATUS,
]
