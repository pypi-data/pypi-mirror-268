import sys

from loguru import logger
import os
import random
import string
import pathlib

from typing import Optional, Tuple


class PbpLogger:
    def __init__(
        self,
        name: str,
        log_filename_and_level: Optional[Tuple[str, str]] = None,
        console_level: Optional[str] = None,
    ):
        """
        Create a logger.

        :param name:
            The name of the logger, typically the date being processed.
        :param log_filename_and_level:
            (filename, level) tuple or None to disable file logging.
        :param console_level:
            The log level for the console, or None to disable console logging.
        """

        self.log_filename_and_level = log_filename_and_level
        self.console_level = console_level

        logger.remove()
        self.logger = logger

        fmt = "{time} {level} {message}"

        if log_filename_and_level is not None:
            log_filename, log_level = log_filename_and_level
            # create log_filename's parent directory if needed:
            parent_dir = pathlib.Path(log_filename).parent
            pathlib.Path(parent_dir).mkdir(parents=True, exist_ok=True)
            file_fmt = fmt
            if os.getenv("EXCLUDE_LOG_TIME", "no") == "yes":
                # test convenience to facilitate local diffing of log files
                file_fmt = "{level} {message}"
            self.logger.add(
                sink=open(log_filename, "w"), level=log_level, format=file_fmt
            )

        if console_level is not None:
            self.logger.add(
                sink=sys.stderr, level=console_level, format=fmt, colorize=True
            )

    def lazy_debug(self, function):
        return self.logger.opt(lazy=True).debug(function)

    def lazy_warn(self, function):
        return self.logger.opt(lazy=True).warning(function)

    def info(self, s: str):
        self.logger.info(s)

    def debug(self, s: str):
        self.logger.debug(s)

    def warn(self, s: str):
        self.logger.warning(s)

    def error(self, s: str):
        self.logger.error(s)

    def exception(self, s: str):
        self.logger.exception(s)


def create_logger(
    log_filename_and_level: Optional[Tuple[str, str]] = None,
    console_level: Optional[str] = None,
) -> PbpLogger:
    """
    Creates a logger. A random name is associated.
    """
    name = "_" + "".join(random.choices(string.ascii_letters, k=7))
    return PbpLogger(name, log_filename_and_level, console_level)
