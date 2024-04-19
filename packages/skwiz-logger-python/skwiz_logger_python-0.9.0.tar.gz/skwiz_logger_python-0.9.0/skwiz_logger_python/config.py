import os

config = {
    "log_level_name": os.environ.get(
        "LOG_LEVEL", "info"
    ),  # (optional) Defines you log level, defaut 'info'
    "log_endpoint": os.environ.get(
        "LOG_ENDPOINT"
    ),  # (optional) Defines an udp endpoint format: 10.0.10.100:5300
    "log_stack_level_name": os.environ.get(
        "LOG_STACK_LEVEL", "error"
    ),  # (optional) Defines minimum level to log stack, default 'error'
    "log_pretty": os.environ.get("LOG_PRETTY")
    == "true",  # (optional) Defines pretty print output, default false
    "log_error_message_length": int(
        os.environ.get("LOG_ERROR_MESSAGE_LENGTH") or "0"
    ),  # (optional) Defines error message max length output, default 0 (no limit)
}
