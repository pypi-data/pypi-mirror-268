import traceback


def is_error(message_object: object):
    return isinstance(message_object, BaseException) or (
        "error" in message_object and isinstance(message_object["error"], BaseException)
    )


def shorten_error_message(error: Exception, max_error_length: int):
    error_message = getattr(error, "message", str(error))
    if max_error_length == 0 or max_error_length is None:
        return error_message

    return error_message[0:max_error_length]


def build_error_message(error: object, max_error_length: int):
    if not is_error(error):
        return error
    error: Exception = error if isinstance(error, Exception) else error["error"]
    return shorten_error_message(error, max_error_length)


def error_serializer(error, max_error_length: int, ignore_stack: bool):
    """Serialize error as bunyan.

    When in doubt, ask what would bunyan do?
    https://github.com/trentm/node-bunyan/blob/master/lib/bunyan.js#L1141
    """
    error_object = {"name": error.__class__.__name__}
    if not ignore_stack:
        if error.__traceback__ is not None:
            trace = "".join(traceback.format_tb(error.__traceback__))
        else:
            # Exceptions that where never caught don't have a stack trace.
            trace = ""
        error_object["stack"] = trace

    error_message = build_error_message(error, max_error_length)
    error_object["message"] = error_message

    return error_object
