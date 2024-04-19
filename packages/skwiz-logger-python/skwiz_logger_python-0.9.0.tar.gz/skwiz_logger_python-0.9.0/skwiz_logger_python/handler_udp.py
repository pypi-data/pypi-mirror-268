import logging.handlers
from logging import LogRecord


class UdpHandler(logging.handlers.DatagramHandler):
    """
    A Datagram Handler with a custom method to make pickle
    """

    def __init__(self, host: str, port: int, formatter):
        logging.handlers.DatagramHandler.__init__(self, host, port)
        self.formatter = formatter

    def makePickle(self, record: LogRecord):
        formatted_record = self.formatter.format(record)
        return formatted_record.encode("utf-8")
