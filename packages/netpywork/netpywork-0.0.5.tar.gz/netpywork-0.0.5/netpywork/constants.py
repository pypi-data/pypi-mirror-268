TUPLE_VERSION = (0,0,5)
VERSION = "".join(str(x) + '.' for x in TUPLE_VERSION)[:-1]
MAX_UDP_PACKET_SIZE = 65507 - 4 - 2 - 4 - 2 - 2
UDP_TIMEOUT = 0.25