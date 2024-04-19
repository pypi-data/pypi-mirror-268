# pylint: disable=no-member
"""
SkwizFormatter

Ensures logs are formatted as we want them.
cfr: https://github.com/sagacify/logger
"""
import datetime
import json
import os
import socket
import sys
from logging import LogRecord

from skwiz_logger_python.colors import color_message
from skwiz_logger_python.error import error_serializer, is_error


def get_name_from_args():
    return (sys.argv[0] or sys.executable).split(os.sep)[-1]


def get_app_name_version():
    main_module = sys.modules["__main__"]
    # If importing from jupyter hub or cli.
    if main_module.__package__ is None:
        return get_name_from_args(), sys.version.split(" ")[0]

    app_package = sys.modules[main_module.__package__]
    try:
        app_name = app_package.__title__
        app_version = app_package.__version__
    except AttributeError:
        app_name = None
        app_version = None

    return app_name, app_version


class SkwizFormatter:
    """
    Skwiz Formatter.

    Formats mesages coming from a skwizlogger
    """

    def __init__(self, log_stack_level: int, max_error_length=0, colorized=False):
        self.app_name, self.app_version = get_app_name_version()
        self.hostname = socket.gethostname()
        self.log_stack_level = log_stack_level
        self.max_error_length = max_error_length
        self.colorized = colorized

    def format(self, record: LogRecord):
        """
        Formats a log record and serializes to json
        """
        level: int = record.levelno
        # By default, "isoformat" outputs 6 digits after the seconds, but
        # Elasticsearch only supports 3 digits (equivalent to milliseconds).
        # "[:-3]" is there to only get milliseconds
        time_iso = (
            datetime.datetime.fromtimestamp(record.created).isoformat()[:-3] + "Z"
        )
        formatted_message = {
            "name": self.app_name,
            "version": self.app_version,
            "module": record.name or record.module,
            "time": time_iso,
            "hostname": self.hostname,
            "pid": record.process,
            "level": level + 10,  # +10 to be coherent with js version of the logger
            "event": record.msg,
        }
        if hasattr(record, "indexed"):
            formatted_message["indexed"] = record.indexed
        if hasattr(record, "raw"):
            formatted_message["raw"] = record.raw
        if hasattr(record, "trace_id"):
            formatted_message["traceId"] = record.trace_id
        if hasattr(record, "request_id"):
            formatted_message["requestId"] = record.request_id

        ignore_stack = level < self.log_stack_level

        json_formatted_message = json.dumps(
            formatted_message,
            default=lambda obj: self.extra_serializer(obj, ignore_stack),
        )
        if self.colorized:
            json_formatted_message = color_message(json_formatted_message, level)
        return json_formatted_message

    def extra_serializer(self, obj: object, ignore_stack: bool):
        """
        A serializer for the json dumping method
        """
        if isinstance(obj, datetime.datetime):
            result = obj.isoformat() + "Z"
        elif isinstance(obj, datetime.date):
            result = obj.isoformat()
        elif isinstance(obj, datetime.time):
            result = obj.strftime("%H:%M")
        elif isinstance(obj, set):
            result = list(obj)[0]
        elif is_error(obj):
            result = error_serializer(obj, self.max_error_length, ignore_stack)
        else:
            result = {"str": str(obj)}
        return result
