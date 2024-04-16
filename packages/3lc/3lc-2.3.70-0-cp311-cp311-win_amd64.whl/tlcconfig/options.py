# =============================================================================
# <copyright>
# Copyright (c) 2023 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================


"""
Configuration options for 3LC

This module contains the configuration options for 3LC. These options can be set in a config file, as environment
variables, or as command line arguments when launching the object service.

"""

from __future__ import annotations

import importlib.metadata
import logging
import os
from typing import Any, Callable, Dict, List

import platformdirs

# CONSTANTS ###################################################################

_logger = logging.getLogger("tlcconfig")


def get_default_root_dir() -> str:
    """Return the default root directory. This directory has a "projects" subdir that contains 3LC projects.

    This function is platform dependent, and the default is platform dependent:

    - Linux: `$HOME/.local/share/3LC/` or `$XDG_DATA_HOME/3LC/`
    - macOS: `$HOME/Library/Application Support/3LC/`
    - Windows: `%LOCALAPPDATA%\\3LC\\3LC\\`

    :returns: The default root directory.
    """

    return platformdirs.user_data_dir(appname="3LC", appauthor="3LC")


def get_default_log_dir() -> str:
    """Return the default log root directory.

    This function is platform dependent, and the default is platform dependent:

    - Linux: `$HOME/.local/state/3LC/log` or `$XDG_STATE_HOME/3LC/log`
    - macOS: `$HOME/Library/Logs/3LC/Logs`
    - Windows: `%LOCALAPPDATA%\\3LC\\3LC\\Logs`

    :returns: The default log root directory.
    """

    return platformdirs.user_log_dir(appname="3LC", appauthor="3LC")


def get_default_config_dir() -> str:
    """Return the default config file directory.

    This function is platform dependent, and the default is platform dependent:

    - Linux: `$HOME/.config/3LC` or `$XDG_CONFIG_HOME/3LC`
    - macOS: `$HOME/Library/Application Support/3LC`
    - Windows: `%LOCALAPPDATA%\\3LC\\3LC`

    :returns: The default config file directory.
    """

    return platformdirs.user_config_dir(appname="3LC", appauthor="3LC")


def _get_default_api_key_file_path() -> str:
    """Return the default API key file path in the config directory.

    :returns: The default API key file path.
    """

    API_KEY_FILE_NAME = "api_key.txt"
    return f"{get_default_config_dir()}{os.path.sep}{API_KEY_FILE_NAME}"


def _get_effective_api_key_file_path() -> str:
    """Return the effective API key file, which will be the default unless overridden by setting TLC_API_KEY_FILE.

    :returns: The effective API key file path.
    """

    return os.environ.get("TLC_API_KEY_FILE", _get_default_api_key_file_path())


def _get_default_telemetry() -> int:
    """Get the default telemetry value.

    If the tlc-enterprise package is installed, telemetry will be disabled by default.

    :returns: The default telemetry value.
    """
    try:
        importlib.metadata.distribution("tlc_enterprise")
        return 0
    except ImportError:
        return 1


def _consider_expandvars(path: str) -> str:
    """Expand a path if it does not begin with a schema definition.

    This function
    E.g. "~/3LC" will be expanded to "/home/user/3LC" on Linux. But s3://~/3LC will not be expanded.
    """
    if not isinstance(path, str):
        raise ValueError(f"Expected string, got {type(path)}")

    if path.find("://") != -1:
        return path
    else:
        expanded_path = os.path.normpath(os.path.expandvars(os.path.expanduser(path)))
        return expanded_path


def _ensure_dir_is_writeable(path: str) -> bool:
    """Ensure that a directory is writeable.

    If the directory starts with a schema (e.g. s3://, https://, etc.), this function will return True.

    If the directory does not exists, it will be created. If it exists, it will be checked for write access.

    :return: True if the directory is writeable, False otherwise.
    """

    if str(path).find("://") != -1:
        return True

    expanded_path = _consider_expandvars(path)

    if not os.path.exists(expanded_path):
        _logger.debug(f"Creating directory {expanded_path}")
        os.makedirs(expanded_path)

    return os.access(expanded_path, os.W_OK)


def _ensure_file_is_writeable(path: str) -> bool:
    """Ensure that a directory for a file is writeable.

    If the directory starts with a schema (e.g. s3://, https://, etc.), this function will return True.

    If the directory does not exists, it will be created. If it exists, it will be checked for write access.

    :return: True if the directory is writeable, False otherwise.
    """

    return _ensure_dir_is_writeable(os.path.dirname(path))


def _any_to_bool(input: Any) -> bool:
    if not isinstance(input, str):
        return bool(input)

    # Define strings that should explicitly return False
    false_strings = ["false", "no", "0", "none", "null", ""]

    # Convert the input string to lower case to make the function case-insensitive
    input_string_lower = input.strip().lower()

    # Check if the input string is in the list of false strings
    if input_string_lower in false_strings:
        return False
    # If not, return True (assuming any string not explicitly false is true)
    else:
        return True


class OPTION:
    """Base class for all 3LC options"""

    default: Any = None
    """The default value for this option if it is not specified anywhere."""

    envvar: str = ""
    """The environment variable to use for this option"""

    key: str = ""
    """The key used for this option in the config file.

    This is the fully qualified key, e.g. "object-server.port" corresponds to the following yaml:
    ```yaml
    object-server:
        port: 5015
    ```

    """

    argument: str = ""
    """The command line argument for this option"""

    data_type: Any = None
    """The type of the option's value"""

    required: bool = False
    """Whether this option is required or not"""

    validate_func: Callable[[Any], bool] | None = None
    """A function to validate the value of this option"""

    transform_func: Callable[[Any], Any] | None = None
    """A function to transform the value of this option before reading it.

    The use case for this is e.g. to expand environment variables or do shell expansion in the value.
    """

    @classmethod
    def class_from_key(cls, key: str) -> type[OPTION]:
        """Get the option class from a key.

        :param key: The key to look up, which should corresponds to the [](OPTION.key) attribute of an option class.
        :returns: The option class corresponding to the key.
        :raises RuntimeError: If the key does not corresponds to a valid option class.
        """
        subclass = [option_class for option_class in cls.__subclasses__() if option_class.key == key]

        if len(subclass) != 1:
            raise RuntimeError(f"Could not find option class for key {key}.")
        else:
            return subclass[0]

    @classmethod
    def is_hidden(cls) -> bool:
        """Whether this option should be hidden or not.

        :returns: True if this option should be hidden, False otherwise.
        """
        return cls.__name__.startswith("_")


class _API_KEY(OPTION):
    """API key to use."""

    default = ""
    key = "api_key"
    data_type = str
    envvar = "TLC_API_KEY"
    argument = "--api-key"


class OBJECT_SERVICE_PORT(OPTION):
    """Port for the server."""

    default = 5015
    key = "service.port"
    data_type = int
    transform_func = int
    envvar = "TLC_SERVICE_PORT"
    argument = "--port"


class OBJECT_SERVICE_DASHBOARD(OPTION):
    """Whether to serve the Dashboard from Object Service."""

    default = False
    key = "service.dashboard"
    data_type = bool
    envvar = "TLC_SERVICE_DASHBOARD"
    argument = "--dashboard"
    transform_func = _any_to_bool
    required = False


class OBJECT_SERVICE_HOST(OPTION):
    """Host for the server."""

    key = "service.host"
    envvar = "TLC_SERVICE_HOST"
    argument = "--host"
    default = "127.0.0.1"
    data_type = str


class OBJECT_SERVICE_LICENSE(OPTION):
    """Specify license or license file

    The option can be either be the license key or point to a local file containing the license key.
    """

    default = ""
    key = "service.license"
    envvar = "TLC_LICENSE"
    argument = "--license"
    data_type = str
    transform_func = lambda x: "" if x is None else str(x)  # noqa: E731


class OBJECT_SERVICE_CACHE_IN_MEMORY_SIZE(OPTION):
    """Specify the amount of memory to use for caching, in bytes.

    Setting the value to 0 will disable in-memory caching.

    Default: 1073741824 (1 GB)
    """

    default = 1073741824
    key = "service.cache_in_memory_size"
    argument = "--cache-size"
    data_type = int


class OBJECT_SERVICE_CACHE_TIME_OUT(OPTION):
    """Specify the cache item time out, in seconds.

    Setting the value to 0 will disable cache eviction based on time.

    Default: 3600 (1 hour)
    """

    default = 3600
    key = "service.cache_time_out"
    argument = "--cache-time-out"
    data_type = int


class PROJECT_ROOT_URL_OPTION(OPTION):
    """Location for reading and writing 3LC data.

    This option is mandatory and must point to a location (e.g. directory on disk or object store bucket) with write
    access. The location will be created if it does not exist.

    If the option value contains an environment variable, it will be expanded.
    """

    default = os.path.join(get_default_root_dir(), "projects")
    """As returned by [](get_default_root_dir)"""

    key = "indexing.project-root-url"
    envvar = "TLC_CONFIG_PROJECT_ROOT_URL"
    argument = "--project-root-url"
    required = True
    data_type = str
    transform_func = _consider_expandvars
    validate_func = _ensure_dir_is_writeable


class PROJECT_SCAN_URLS_OPTION(OPTION):
    """Locations to scan for 3LC objects (runs and tables) following a standard 3LC project layout.

    Usually a 'projects' directory containing multiple projects. Default directories will be created if they do not
    exist.
    """

    default = []
    key = "indexing.project-scan-urls"
    data_type = List[str]
    transform_func = _consider_expandvars


class EXTRA_TABLE_SCAN_URLS_OPTION(OPTION):
    """Extra (non-recursive) locations to scan for 3LC Table objects.

    This option allows searching individual folders/locations for 3LC Table objects outside the standard hierarchy of a
    3LC project structure. For example:
     - "C:\\Users\\user\\Documents\\3LC\\tables"
     - "s3://my-bucket/3LC/tables".

    Note: these locations will not be scanned recursively.

    Indexed Tables from these extra locations can be used interchangeably with other Tables discovered by the system.
    """

    default = []
    key = "indexing.extra-table-scan-urls"
    data_type = List[str]
    transform_func = _consider_expandvars


class EXTRA_RUN_SCAN_URLS_OPTION(OPTION):
    """Extra (non-recursive) locations to scan for 3LC Run objects.

    This option allows searching individual folders/locations for 3LC Run objects outside the standard hierarchy of a
    3LC project structure. For example:
     - "C:\\Users\\user\\Documents\\3LC\\runs"
     - "s3://my-bucket/3LC/runs".

    Note: these locations will not be scanned recursively.

    Indexed Runs from these extra locations can be used interchangeably with other Runs discovered by the system.
    """

    default = []
    key = "indexing.extra-run-scan-urls"
    data_type = List[str]
    transform_func = _consider_expandvars


class LOGFILE(OPTION):
    """Log file for the 3LC logger.

    The directory will be created if it does not exist.

    If the option value contains an environment variable, it will be expanded.
    """

    default = os.path.join(get_default_log_dir(), "3LC.log")
    """As returned by [](get_default_log_dir) / 3LC.log"""

    key = "logging.logfile"
    envvar = "TLC_LOGFILE"
    argument = "--logfile"
    data_type = str
    transform_func = _consider_expandvars
    validate_func = _ensure_file_is_writeable


class LOGLEVEL(OPTION):
    """Log level for the 3LC logger.

    The `tlc` Python package adheres to the standard Python logging levels:

      - DEBUG:  Detailed information, typically of interest only when diagnosing problems.
      - INFO: Confirmation that things are working as expected.
      - WARNING: An indication that something unexpected happened, or indicative of some problem in the near future
        (e.g. "disk space low"). The software is still working as expected.
      - ERROR: Due to a more serious problem, the software has not been able to perform some function.
      - CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
    """

    default = "WARNING"
    key = "logging.loglevel"
    envvar = "TLC_LOGLEVEL"
    argument = "--loglevel"
    transform_func = str.upper
    validate_func = lambda x: x in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]  # noqa: E731


class DISPLAY_PROGRESS(OPTION):
    """Whether to display progress bars or not.

    The option can be either 0 or 1, where 0 means no progress bars and 1 means progress bars.
    """

    default = 1
    data_type = int
    transform_func = int
    key = "tlc.display-progress"
    envvar = "TLC_DISPLAY_PROGRESS"
    argument = "--display-progress"
    validate_func = lambda x: x in [0, 1]  # noqa: E731


class TELEMETRY(OPTION):
    """Whether to send Telemetry or not."""

    default = _get_default_telemetry()
    data_type = int
    key = "tlc.telemetry"
    envvar = "TLC_TELEMETRY"
    argument = "--telemetry"
    transform_func = int


class _SENTRY_DSN(OPTION):
    """Sentry DSN."""

    _python_package_dsn = (
        "https://96261883d7e59c8a0c8d23f97ebc4466@o4507034839285760.ingest.de.sentry.io/4507035033665616"
    )
    _object_service_dsn = (
        "https://2b118a64f29ece64bb4b60bb0f098099@o4507034839285760.ingest.de.sentry.io/4507035023048784"
    )

    default = _python_package_dsn
    data_type = str
    key = "tlc.sentry-dsn"
    envvar = "TLC_SENTRY_DSN"


class ALIASES(OPTION):
    """List of aliases."""

    default = {}
    data_type = Dict[str, str]
    key = "aliases"
    transform_func = _consider_expandvars


class _SERIALIZATION_CHECK_OVERRIDE(OPTION):
    """Whether to override the serialization check override."""

    default = False
    data_type = bool
    key = "tlc.serialization-check-override"
    transform_func = _any_to_bool
    envvar = "TLC_SERIALIZATION_CHECK_OVERRIDE"
