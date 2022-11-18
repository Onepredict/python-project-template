"""
Make Logger instance.

Author:
    Kibum Park
E-mail:
    castedice1@gmail.com
"""

import logging
import sys
from pathlib import Path
from types import TracebackType
from typing import Any, Optional

LOG_DIR_PATH = Path("./log")
LOG_DIR_PATH.mkdir(exist_ok=True, parents=True)
LOG_PATH = LOG_DIR_PATH / "log.log"
LOG_FORMAT = (
    "[%(asctime)s] %(levelname)-8s >> "  # noqa: WPS323
    + "%(name)s : %(lineno)4s - %(message)s"  # noqa: WPS323
)


class ConsoleFormatter(logging.Formatter):
    """Format logs for console."""

    blue = "\x1b[34;20m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    formats = {
        logging.DEBUG: blue + LOG_FORMAT + reset,
        logging.INFO: grey + LOG_FORMAT + reset,
        logging.WARNING: yellow + LOG_FORMAT + reset,
        logging.ERROR: red + LOG_FORMAT + reset,
        logging.CRITICAL: bold_red + LOG_FORMAT + reset,
    }

    def format(self, record: logging.LogRecord) -> str:
        """Make format for console.

        Override `logging.LogRecord`

        Args:
            record (logging.LogRecord) : `logging.LogRecord` module.

        Returns:
            str : Formatted logs.

        # noqa: DAR101 arg1
        """
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def make_logger(name: Optional[str]) -> logging.Logger:
    """Make logger instance.

    Only using `% formatting`, not f-string, format string.
    Format is`[YYYY-MM-DD hh:mm:ss,ms] <LEVEL>  >> <FILENAME> : <LINENO> - <MESSAGE>`

    Args:
        name (str, optional): Set `__name__` when calling logger.

    Returns:
        logging.Logger: Logging instance.
    """
    logger = logging.getLogger(name)
    logger.propagate = False
    if name == "":
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console_formatter = ConsoleFormatter()
    console.setFormatter(console_formatter)
    logger.addHandler(console)

    file_handler = logging.FileHandler(filename=LOG_PATH)
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger


def hook_exception(
    exc_type: Any,
    exc_value: BaseException,
    exc_traceback: Optional[TracebackType],
) -> None:
    """Catch exception when unexpected exceptions occur.

    Args:
        exc_type (Any): Exception type.
        exc_value (BaseException): Exception value.
        exc_traceback (TracebackType, optional): Traceback.
    """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

    logger.exception(
        "Unexpected exception",
        exc_info=(exc_type, exc_value, exc_traceback),
    )


logger = make_logger("")
sys.excepthook = hook_exception
