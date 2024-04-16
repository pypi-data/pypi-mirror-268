# =============================================================================
# <copyright>
# Copyright (c) 2023 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================

"""Logging configuration for the 3LC module, supporting default and customizable configurations."""

from __future__ import annotations

import logging.config
import os
import sys
from typing import Any

from termcolor import colored

import tlcconfig.options as options
from tlcconfig.option_loader import OptionLoader

# CONSTANTS ###################################################################

_STREAM_HANDLER_PREFIX = "tlc: "
_DATE_FMT = "%m/%d %H:%M:%S"


def default_log_file_handler() -> dict[str, Any]:
    """Returns the default log fileHandler"""
    dictConfig = {
        "formatters": {
            "tlc_file_formatter": {
                "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
            },
        },
        "handlers": {
            "tlc_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": options.LOGFILE.default,
                "formatter": "tlc_file_formatter",
            },
        },
    }

    return dictConfig


def default_dictConfig() -> dict:
    """Return the default configuration for the 3LC logger.

    This function return the base logging config, that can be adapted by a LoggerConfigurator instance.

    Returns: A dict compatible with the logging.config.dictConfig() function.
    """
    dictConfig = {
        "version": 1,
        "disable_existing_loggers": False,  # To avoid removing any other loggers that the user may have configured.
        "formatters": {
            "tlc_colorful_formatter": {
                "class": "tlcconfig.logger_configurator._ColorfulFormatter",
                "format": colored(_STREAM_HANDLER_PREFIX, "light_green") + "%(message)s",
                "datefmt": _DATE_FMT,
            },
        },
        "handlers": {
            "tlc_stream_handler": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "tlc_colorful_formatter",
            },
        },
        "loggers": {
            "tlc": {
                "level": OptionLoader.instance().get_value(options.LOGLEVEL),
                # Notice that the default handler does not include the disk logfile. This is so that
                # when using the notebook API naively, it will not log to disk.
                "handlers": ["tlc_stream_handler"],
                "propagate": False,
            }
        },
    }
    return dictConfig


class LoggerConfigurator:
    """LoggerConfigurator provide an interface to configure the 3LC logger prior to importing the tlc module.

    LoggerConfigurator provides an interface to configure a dictionary which corresponds to version 1 of the
    [dictConfig](inv:python#logging.config.dictConfig) API. An instance of such a dictionary can be set as a class
    variable on the LoggerConfigurator-class, and it will be used to configure the 3LC logger when the tlc module is
    imported.

    Once a dictConfig is fully configured, the user must call
    [initialize_logging_config](#tlcconfig.logger_configurator.LoggerConfigurator.initialize_logging_config) in order to
    set the class variable that will be used to configure the 3LC logger.

    It is possible to initialize the class with a custom dictConfig to, the user is
    then fully responsible for this dictConfig to be valid.
    """

    _instance: LoggerConfigurator | None = None

    def __init__(self, dictConfig: dict[str, Any] | None = None) -> None:
        if dictConfig is None:
            dictConfig = default_dictConfig()
        self.dictConfig = dictConfig
        self._applied = False

    def initialize_logging_config(self, incremental: bool = False, force: bool = False) -> None:
        """Initialize the Python [logging](inv:python#logging) system with this configuration.

        Initializing configuration should be a one-time operation done on startup.  Invoking this method multiples times
        will have no effect unless the `force` parameter is set to True.

        :param incremental: If True, the configuration will be applied incrementally. See the Python [logging config
        documentation](inv:python#logging.config) for more details about incremental configuration.

        :param force: If True, the configuration will be applied even if it has already been applied.
        """

        if not self._applied or force:
            effective_dictConfig = {**self.dictConfig, "incremental": incremental}
            logging.config.dictConfig(effective_dictConfig)

        if not self._applied:
            self._applied = True

    @staticmethod
    def instance() -> LoggerConfigurator:
        """Returns the singleton LoggerConfigurator object."""
        if LoggerConfigurator._instance is None:
            LoggerConfigurator._instance = LoggerConfigurator()

        return LoggerConfigurator._instance

    def set_log_level(self, log_level: str) -> None:
        """Set the log level for the 3LC logger.

        :param log_level: The log level to set. Must be one of "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL".
        """

        self.dictConfig["loggers"]["tlc"]["level"] = log_level

    def enable_log_file(self) -> None:
        """Enable use of a logfile for the 3LC logger."""

        logfileDictConfig = default_log_file_handler()

        # Check if the user has set a custom logfile location.
        option_loader = OptionLoader.instance()
        if option_loader:
            effective_logfile = str(option_loader.get_value(options.LOGFILE))
            logfileDictConfig["handlers"]["tlc_file_handler"]["filename"] = effective_logfile

        logfile = logfileDictConfig["handlers"]["tlc_file_handler"]["filename"]

        logDirectory = os.path.dirname(logfile)
        try:
            # Make sure the log directory exists.
            os.makedirs(logDirectory, exist_ok=True)

            self.dictConfig["handlers"].update(logfileDictConfig["handlers"])
            self.dictConfig["formatters"].update(logfileDictConfig["formatters"])
            self.dictConfig["loggers"]["tlc"]["handlers"].append("tlc_file_handler")
        except Exception as e:
            print(f"Unable to create logfile directory: {logDirectory}.\nDetails: {e}", file=sys.stderr)

    def get_current_log_file_path(self) -> str:
        """Returns the current log file path, if any.

        :returns: The current log file path, or an empty string if no log file is configured.
        """

        if "tlc_file_handler" in self.dictConfig["handlers"]:
            return self.dictConfig["handlers"]["tlc_file_handler"]["filename"]
        return ""

    @staticmethod
    def get_next_log_level(current_log_level: str) -> str:
        """Returns the next log level in the sequence.

        :param current_log_level: The current log level. Must be one of "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL".
        :returns: The next log level in the sequence "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL".
        :raises ValueError: If the current log level is not one of "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL".
        """

        levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if current_log_level not in levels:
            raise ValueError(f"Unknown log level: {current_log_level}")
        return levels[(levels.index(current_log_level) + 1) % len(levels)]


class _ColorfulFormatter(logging.Formatter):
    def formatMessage(self, record: logging.LogRecord) -> str:
        log = super().formatMessage(record)
        if record.levelno == logging.WARNING:
            prefix = colored("WARNING", "red", attrs=["blink"])
        elif record.levelno == logging.ERROR or record.levelno == logging.CRITICAL:
            prefix = colored("ERROR", "red", attrs=["blink", "underline"])
        else:
            return log
        return prefix + " " + log
