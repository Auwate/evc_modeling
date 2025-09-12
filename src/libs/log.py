"""
The logging class
"""

import os
import logging
from typing import Dict

from enum import Enum

class LoggerType(Enum):
    """
    An enum mapper for usage on mapping log level to int
    """
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARN = logging.WARN
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

class Log:
    """
    Logger class
    """
    _FORMAT = '%(asctime)s %(class)-8s %(message)s'

    def __init__(self, class_name: str = "N/A", log_level: str = "INFO", ):

        if not logging.getLogger().handlers:
            logging.basicConfig(format=Log._FORMAT)

        extra: Dict[str, str] = {"class": class_name}

        self._logger: logging.LoggerAdapter = self._create_logger(
            level=self._get_level(log_level),
            extra=extra
        )

    # Public

    def debug(self, message: str) -> None:
        """
        Log a debug message to the level provided at startup
        """
        self._logger.debug(msg=message)

    def info(self, message: str) -> None:
        """
        Log an info message to the level provided as an env variable
        """
        self._logger.info(msg=message)

    def warn(self, message: str) -> None:
        """
        Log a warning message
        """
        self._logger.warning(msg=message)

    def error(self, message: str) -> None:
        """
        Log an error message
        """
        self._logger.error(msg=message)

    def critical(self, message: str) -> None:
        """
        Log a critical error message
        """
        self._logger.critical(msg=message)

    # Private

    def _get_level(self, level: str) -> LoggerType:
        """
        A try-catch block to map the level in string format to int
        """
        try:
            level: str = level.upper()
            return LoggerType[level]
        except KeyError as exc:
            print(f"Invalid logging level '{level}'. Available levels include:")
            for log_level in LoggerType.__members__:
                print(f"- {log_level}")
            raise exc
        except Exception as exc:
            raise exc

    def _create_logger(self, level: LoggerType, extra: Dict[str, str]) -> logging.LoggerAdapter:
        """
        Create a logger, as well as setting its appropriate levels
        """
        new_logger = logging.Logger(name="logger")
        new_logger.setLevel(level=level.value)
        return logging.LoggerAdapter(logger=new_logger, extra=extra)
