import logging
import sys

from saga_logger import config
from saga_logger.formatter import SagaFormatter
from saga_logger.handler_udp import UdpHandler

LOG_LEVELS = {
    "fatal": 50,
    "error": 40,
    "warning": 30,
    "warn": 30,
    "info": 20,
    "debug": 10,
    "trace": 0,
}


def setup():
    log_level = LOG_LEVELS[config["log_level_name"].lower()]

    log_stack_level = LOG_LEVELS[config["log_stack_level_name"].lower()]

    root_logger = logging.root
    root_logger.setLevel(log_level)

    log_formatter = SagaFormatter(
        log_stack_level, config["log_error_message_length"], config["log_pretty"]
    )

    if config["log_endpoint"] is not None:
        [host, port] = config["log_endpoint"].split(":")
        # Udp handler must be formatted manually as the automatic formatting
        # does not seem to work
        log_handler = UdpHandler(host, int(port), log_formatter)
    else:
        log_handler = logging.StreamHandler(stream=sys.stdout)
        log_handler.setFormatter(log_formatter)

    root_logger.addHandler(log_handler)


class SagaLogger:
    setup_done = False

    def __init__(self, module: str = None, extra=None):
        # Setup the logging on root if not already done
        if not SagaLogger.setup_done:
            setup()
            SagaLogger.setup_done = True

        self.logger = logging.getLogger(module)
        self.extra = extra if extra else {}

    def trace(self, message: str, index: dict = None, raw: dict = None):
        self.logger.trace(
            message, extra=dict(self.extra, **{"indexed": index, "raw": raw})
        )

    def debug(self, message: str, index: dict = None, raw: dict = None):
        self.logger.debug(
            message, extra=dict(self.extra, **{"indexed": index, "raw": raw})
        )

    def info(self, message: str, index: dict = None, raw: dict = None):
        self.logger.info(
            message, extra=dict(self.extra, **{"indexed": index, "raw": raw})
        )

    def warn(self, message: str, index: dict = None, raw: dict = None):
        self.logger.warning(
            message, extra=dict(self.extra, **{"indexed": index, "raw": raw})
        )

    def error(self, message: str, index: dict = None, raw: dict = None):
        self.logger.error(
            message, extra=dict(self.extra, **{"indexed": index, "raw": raw})
        )

    def fatal(self, message: str, index: dict = None, raw: dict = None):
        self.logger.fatal(
            message, extra=dict(self.extra, **{"indexed": index, "raw": raw})
        )
