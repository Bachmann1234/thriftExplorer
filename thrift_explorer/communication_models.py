from enum import Enum
import attr

"""
    Here are some things I can theoredically support
    but am punting on until I am further along
    timeout
    certificates/ssl
    timeouts (not sure I want this one)
    http vs rpc (currently supporting just rpc)
    unix socket rather than server
    finagle protocol
    mutliplex protocol
"""


class Protocol(Enum):
    BINARY = "binary"
    JSON = "json"
    COMPACT = "compact"

    @staticmethod
    def from_string(input_string):
        return Protocol(input_string.lower().strip())


class Transport(Enum):
    BUFFERED = "buffered"
    FRAMED = "framed"

    @staticmethod
    def from_string(input_string):
        return Transport(input_string.lower().strip())


@attr.s(frozen=True)
class ThriftRequest(object):
    """
    The model containing all the information necessary to make a thrift request
        thrift_file: str
            The thrift where the service being called is defined
        service_name: str
            Name of the service being called 
        endpoint_name: str
            Endpoint being requested
        host: str
            Hostname (or IP) where the service is hosted
        port: int (or string that is an int)
            Port of the service being hit
        protocol (string, gets converted to a Protocol):
            One of the supported thrift protocols
                BINARY
                JSON
                COMPACT
                MULTIPLEXED
        transport (string, gets converted to a Transport):
            One of the supported thrift transports
                BUFFERED
                FRAMED
        request_body dict:
            dictionary that represents the request being made. Its structure
            is dependent on the request being made
    """

    thrift_file = attr.ib()
    service_name = attr.ib()
    endpoint_name = attr.ib()
    host = attr.ib()
    port = attr.ib(converter=int)
    protocol = attr.ib(converter=Protocol.from_string)
    transport = attr.ib(converter=Transport.from_string)
    request_body = attr.ib(default=attr.Factory(dict))
