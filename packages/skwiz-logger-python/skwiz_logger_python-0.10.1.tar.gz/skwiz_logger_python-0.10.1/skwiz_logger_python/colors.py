GREY = "\x1b[38;20m"
YELLOW = "\x1b[33;20m"
RED = "\x1b[31;20m"
BOLD_RED = "\x1b[31;1m"
RESET = "\x1b[0m"


def color_message(message: str, log_level: int):
    if log_level in [0, 10, 20]:
        return GREY + message + RESET
    if log_level == 30:
        return YELLOW + message + RESET
    if log_level == 40:
        return RED + message + RESET
    if log_level == 50:
        return BOLD_RED + message + RESET
    return message
