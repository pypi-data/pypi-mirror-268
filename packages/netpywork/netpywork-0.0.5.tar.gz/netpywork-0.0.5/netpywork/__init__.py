from .constants import *
from .server import *
from .client import *
from .protocol import *
from datetime import timedelta

__version__ = VERSION
udp_storetime: timedelta = timedelta(minutes=1)