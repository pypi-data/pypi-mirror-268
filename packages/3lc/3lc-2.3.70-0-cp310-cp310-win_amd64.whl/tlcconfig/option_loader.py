# =============================================================================
# <copyright>
# Copyright (c) 2023 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================

"""This module contains the OptionLoader class, which is used to load and store the 3LC options."""

# IMPORTS #####################################################################

from __future__ import annotations

import datetime
import logging
import os
from enum import Enum
from io import StringIO
from typing import Any, get_origin

import ruamel.yaml

import tlcconfig.options as options

# CONSTANTS ###################################################################

_CONFIG_FILE_HEADER = f"""
# Configuration file for `tlc`.
#
# This YAML file contains setting for the `tlc` Python Package.
# Created at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

"""

_logger = logging.getLogger("tlcconfig")

# FUNCTIONS ###################################################################


def get_default_config_file() -> str:
    """Return the default config file."""

    filename = "config.yaml"

    return os.path.join(options.get_default_config_dir(), filename)


def get_default_config_file_locations() -> list[str]:
    """Return the default config file location."""

    filename = "config.yaml"
    candidates = [
        os.path.join(os.getcwd(), filename),
        get_default_config_file(),
    ]

    return candidates


# CLASSES #####################################################################


class ConfigSource(Enum):
    """The source of an option's value.

    This enum is used during option resolution to track and store from which source the option was set.
    """

    DEFAULT = 0
    """The option was set with the default value."""
    CONFIG_FILE = 1
    """The option was loaded from a configuration file."""
    ENVIRONMENT = 2
    """The option was loaded from an environment variable."""
    COMMAND_LINE = 3
    """The option was set on the command line."""
    API = 4
    """The option was set using the API."""


class OptionValue:
    """Holds the value of a 3LC option"""

    def __init__(self, cls: type[options.OPTION]):
        self.cls = cls
        self._set(cls.default, ConfigSource.DEFAULT)

    def _set(self, value: Any, config_source: ConfigSource) -> None:
        """Set the value of the option."""

        try:
            transformed_value = self._transform(value)
            if self.cls.data_type is not None and not isinstance(
                transformed_value, get_origin(self.cls.data_type) or self.cls.data_type
            ):
                raise ValueError(
                    f"type mismatch, expected {get_origin(self.cls.data_type) or self.cls.data_type}"
                    + f" got {type(transformed_value)}"
                )

            if self.cls.required and transformed_value is None:
                raise ValueError("Missing required option")
            if self.cls.validate_func and not self.cls.validate_func(transformed_value):
                if transformed_value != value:
                    raise ValueError(
                        f"invalid value: {transformed_value} ({type(transformed_value)}),"
                        + f" transformed from original value: {value} ({type(value)})"
                    )
                else:
                    raise ValueError(f"invalid value: {value} ({type(value)})")

            self.value = transformed_value
            self.config_source = config_source

        except Exception as exc:
            msg = f"Could not set 3LC option {self.cls.__name__},"
            if config_source == ConfigSource.CONFIG_FILE:
                msg += " check config file for error"
            elif config_source == ConfigSource.ENVIRONMENT:
                msg += f" check environment variable {self.cls.envvar} for error"
            elif config_source == ConfigSource.COMMAND_LINE:
                msg += f" check command line {self.cls.argument} for error"
            help = f". Option help:\n{self.cls.__doc__}" if self.cls.__doc__ else ""
            raise ValueError(msg + f": {exc}" + help)

    def _transform(self, value: Any) -> Any:
        """Apply any transform function to an input  value.

        This method will also wrap the transform function around lists and dicts"""

        if value is None:
            # handle yaml conversion of empty lists/dicts to None
            if (self.cls.data_type is list) or (get_origin(self.cls.data_type) is list):
                return []
            elif (self.cls.data_type is dict) or (get_origin(self.cls.data_type) is dict):
                return {}

        if not self.cls.transform_func:
            return value

        if isinstance(value, list):
            return [self.cls.transform_func(v) for v in value]
        elif isinstance(value, dict):
            return {k: self.cls.transform_func(v) for k, v in value.items()}

        return self.cls.transform_func(value)


class OptionLoader:
    """Load the 3LC options.

    :::{note}
        Even if config_file is passed in, values from environment variables will override values from the config file.
    :::

    :param config_file: The config file to use. If None, the default config files will be searched for and used if they
                        exist.
    :param initialize: If True, the options will be read from the config file and environment variables. This is the
                       default.

    :raises FileNotFoundError: If config_file is set and does not exists.
    """

    _instance: OptionLoader | None = None

    def __init__(self, config_file: str | None = None, initialize: bool = True) -> None:
        self._option_values: dict[type[options.OPTION], OptionValue] = {}

        # the file that the file config was loaded from
        self._config_file: str | None = None

        for cls in options.OPTION.__subclasses__():
            self._option_values[cls] = OptionValue(cls)

        effective_config_file: str | None = None

        if initialize:
            if config_file:
                if not os.path.exists(config_file):
                    raise FileNotFoundError(f"Config file '{config_file}' does not exist.")
                else:
                    effective_config_file = config_file
            else:
                effective_config_file = OptionLoader.resolve_effective_config_file()

            if effective_config_file:
                self.update_from_yaml_file(effective_config_file)

            self.update_from_environment()

    @property
    def config_file(self) -> str | None:
        return self._config_file

    def get_config(self) -> dict[type[options.OPTION], Any]:
        """Return the current configuration as a dictionary."""
        d = {}
        for key, value in self._option_values.items():
            d[key] = value.value

        return d

    def get_value(self, option: type[options.OPTION]) -> Any:
        """Return the value of an option."""
        return self._option_values[option].value

    def get_config_source(self, option: type[options.OPTION]) -> ConfigSource:
        """Return the value of an option."""
        return self._option_values[option].config_source

    def set_value(
        self, option: type[options.OPTION], value: Any, config_source: ConfigSource = ConfigSource.API
    ) -> None:
        """Set the value of an option."""
        self._update(option, value, config_source)

    def to_yaml(self) -> str:
        """Return the current configuration as a YAML string."""

        nested_dict = ruamel.yaml.comments.CommentedMap()

        for option, option_value in self._option_values.items():
            # Hide options that start with an underscore
            if option.is_hidden():
                continue

            parts = option.key.split(".")
            current_dict = nested_dict

            for part in parts[:-1]:
                if part not in current_dict:
                    current_dict[part] = ruamel.yaml.comments.CommentedMap()
                current_dict = current_dict[part]

            current_dict[parts[-1]] = option_value.value
            column = 50

            # Add docstring as comment
            lines = str(option.__doc__).splitlines()

            # Multi-line docstrings
            if len(lines) > 1:
                # Format __doc__ so it looks nicer as a yaml comment.
                formatted_doc = str(option.__doc__).replace("\n\n", "\n \n").replace("    ", "")
                current_dict.yaml_set_comment_before_after_key(parts[-1], before="\n" + formatted_doc, indent=2)
            # Long single-line docstrings
            elif len(parts[-1]) + len(lines[0]) > column:
                current_dict.yaml_set_comment_before_after_key(parts[-1], before="\n" + lines[0], indent=2)
            else:
                current_dict.yaml_set_comment_before_after_key(parts[-1], before="\n")
                current_dict.yaml_add_eol_comment(lines[0], parts[-1], column=column)

        nested_dict.yaml_set_start_comment(_CONFIG_FILE_HEADER)

        # Add "section-header" to each top-level section
        for key in nested_dict.keys():
            title_key = key.replace("-", " ").title()
            nested_dict.yaml_set_comment_before_after_key(key, f"\n{title_key} Settings")

        yaml = ruamel.yaml.YAML()
        yaml.indent(mapping=2, sequence=0, offset=2)

        output = StringIO()
        yaml.dump(nested_dict, output)

        return output.getvalue()

    def write_to_yaml_file(self, filename: str, overwrite: bool = False) -> None:
        """Write the current configuration to a YAML file.

        :param filename: The name of the file to write to, if not set the default config file will be used as returned
            by [](get_default_config_file).
        :param overwrite: If True, the file will be overwritten if it exists. If False, the file will not be written.
        """
        if os.path.exists(filename) and not overwrite:
            return

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        _logger.debug(f"Writing configuration to {filename}")
        with open(filename, "w") as f:
            f.write(self.to_yaml())

    def _update(self, cls: type[options.OPTION], value: Any, config_source: ConfigSource) -> None:
        """Update the value of key in the configuration."""

        self._option_values[cls]._set(value, config_source)

    @staticmethod
    def _append_key(base_key: str, sub_key: str) -> str:
        if base_key:
            return base_key + "." + sub_key
        else:
            return sub_key

    def _update_from_dict_helper(self, config: dict[str, Any], base_key: str, config_source: ConfigSource) -> None:
        """Recursively update the configuration from a nested dictionary.

        An unknown key will be silently ignored. Incorrect values will raise a ValueError.

        :raises ValueError: If an incorrect value is encountered.
        """
        for sub_key, value in config.items():
            full_key = self._append_key(base_key, sub_key)

            # If the data-type of a OPTION is "dict", this means we should not recurse into it,
            # but instead treat it as a single value.
            cls = None
            try:
                cls = options.OPTION.class_from_key(full_key)
            except RuntimeError:
                pass

            if cls:
                self._update(cls, value, config_source)
            else:
                if isinstance(value, dict):
                    self._update_from_dict_helper(value, full_key, config_source)
                else:
                    _logger.warning(f"Ignoring unknown configuration option: {full_key}")

    def _update_from_yaml_dict(
        self,
        config: dict[str, Any],
    ) -> None:
        """Update the configuration from a dictionary in yaml format.

        This method is intended to be used to update the configuration from a YAML file.
        """
        self._update_from_dict_helper(config, "", ConfigSource.CONFIG_FILE)

    def update_from_yaml_file(self, config_file: str) -> None:
        """Update the configuration from a YAML file."""
        _logger.debug(f"Loading configuration from {config_file}")
        config = OptionLoader._yaml_config_file_to_dict(config_file)
        self._update_from_yaml_dict(config)
        self._config_file = config_file

    def update_from_environment(self) -> None:
        """Update the configuration from the environment."""
        self._update_from_environment(dict(os.environ))

    def _update_from_environment(self, environ: dict[str, str]) -> None:
        for cls in options.OPTION.__subclasses__():
            if cls.envvar in environ:
                if cls.is_hidden():
                    _logger.debug(f"Loading configuration from environment variable {cls.envvar}")
                else:
                    _logger.debug(
                        f"Loading configuration from environment variable {cls.envvar} = {environ[cls.envvar]}"
                    )
                self._update(cls, environ[cls.envvar], ConfigSource.ENVIRONMENT)

    @staticmethod
    def _yaml_config_file_to_dict(config_file: str) -> dict[str, Any]:
        """Load the configuration from a YAML file."""
        with open(config_file) as f:
            yaml = ruamel.yaml.YAML(typ="safe", pure=True)
            config = yaml.load(f)
        return config

    @staticmethod
    def set_instance(option_loader: OptionLoader, write_config_file: bool = True) -> None:
        """Set the instance of the OptionLoader to be used by the rest of the package.

        :param option_loader: The OptionLoader instance to be used by the rest of the application.
        :param write_config_file: If True, the default config file will be written if no config file was set.
        """

        OptionLoader._instance = option_loader

        if write_config_file and not option_loader._config_file:
            option_loader.write_to_yaml_file(get_default_config_file())

    @staticmethod
    def instance() -> OptionLoader:
        """Return the instance of the OptionLoader to be used by the rest of the application.

        If the instance has not been set, a new instance will be created using the defaults.

        :returns: The OptionLoader instance to be used by the rest of the application.
        :raises ValueError: If no valid OptionLoader can be created.
        """
        if OptionLoader._instance is None:
            option_loader = OptionLoader()
            OptionLoader.set_instance(option_loader)  # This will check if the default config file should be written.

        return OptionLoader._instance  # type: ignore

    @staticmethod
    def resolve_effective_config_file(path: str | None = None, env: dict[str, str] | None = None) -> str | None:
        """Return the effective config file path.

        This method will search for a valid config file in the following order:

        - Path specified by the path argument
        - Path specified by the TLC_CONFIG_FILE environment variable
        - Default config file locations

        :param path: The path to the config file to use. If None, the default config files will be searched for.
        :param env: Dict for environment variables. If None, os.environ will be used.
        :return: A string with a path to a config file. Returns None if no config file can be found.
        :raises FileNotFoundError: If the path argument or TLC_CONFIG_FILE environment variable is specified but the
                                   file does not exist.
        """

        if not env:
            env = dict(os.environ)

        if path is not None:
            if not path.strip():
                return ""  # treat empty str as disabled config file
            elif os.path.exists(path):
                return path
            else:
                raise FileNotFoundError(f"Config file {path} does not exist")

        config_file_from_env = env.get("TLC_CONFIG_FILE")
        if config_file_from_env is not None:
            if not config_file_from_env.strip():
                _logger.debug("Env TLC_CONFIG_FILE is set but empty, aborting config file resolving.")
                return ""  # treat empty string as no config file
            if os.path.exists(config_file_from_env):
                return config_file_from_env
            else:
                raise FileNotFoundError(
                    f"File specified in environment variable TLC_CONFIG_FILE {config_file_from_env} does not exist"
                )

        # Check for filesize here handles the case where the user is running e.g.
        # 3lc config --to-yaml > config.yaml
        # In this case, the empty file handle will already be created by the time we load config files.
        for candidate in get_default_config_file_locations():
            if os.path.exists(candidate) and os.path.getsize(candidate) > 0:
                return candidate

        return None
