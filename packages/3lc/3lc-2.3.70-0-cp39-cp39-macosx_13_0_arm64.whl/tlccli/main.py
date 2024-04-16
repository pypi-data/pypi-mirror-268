# =============================================================================
# <copyright>
# Copyright (c) 2023 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================

"""Command Line Interface for 3LC."""

from __future__ import annotations

import argparse
import logging
import sys
from typing import Any, Sequence, TypeVar

import tlcconfig.options as options
from tlcconfig.logger_configurator import LoggerConfigurator
from tlcconfig.option_loader import ConfigSource, OptionLoader
from tlcconfig.version import _PACKAGE_GIT_REVISION, _PACKAGE_VERSION

from tlccli.subcommands.config import ConfigSubCommand
from tlccli.subcommands.export import ExportSubCommand
from tlccli.subcommands.login import LoginSubCommand
from tlccli.subcommands.object_service import ObjectServiceSubCommand

NamespaceType = TypeVar("NamespaceType")


class NoConfigFileAction(argparse.Action):
    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: NamespaceType,
        values: str | None,  # type: ignore
        option_string: str | None = None,
    ) -> None:
        # Set config-file to an empty string when --no-config-file is used
        setattr(namespace, "config_file", "")


def create_parser(add_help: bool = True) -> argparse.ArgumentParser:
    """Create the argument parser for the early arguments."""

    parser = argparse.ArgumentParser(
        # description="Launch the 3LC object service",
        # epilog="See the docs at https://docs.3lc.ai/ for more details",
        add_help=add_help,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"{parser.prog} {_PACKAGE_VERSION} Git revision: {_PACKAGE_GIT_REVISION}",
        help="Print the version information and exit.",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity level. Include multiple times for more detail (e.g., -vvv).",
    )

    config_file_group = parser.add_mutually_exclusive_group()
    config_file_group.add_argument(
        "--config-file",
        help="Specify the config file path, if not set will resort to the default locations",
        default=None,
    )
    config_file_group.add_argument(
        "--no-config-file",
        help="Do not load any config file, only load configuration from command line and environment variables.",
        action=NoConfigFileAction,
        nargs=0,
    )

    return parser


class ConfigOptionAction(argparse.Action):
    option_loader: OptionLoader | None = None

    def __init__(self, option_strings: Sequence[str], dest: str, nargs: int | str | None = None, **kwargs: Any) -> None:
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(
        self,
        parse: Any,
        namespace: Any,
        values: Any,
        option_string: Any = None,
    ) -> None:
        option_class = options.OPTION.class_from_key(self.dest)
        if ConfigOptionAction.option_loader:
            ConfigOptionAction.option_loader._update(option_class, values, ConfigSource.COMMAND_LINE)

        setattr(namespace, self.dest, values)


def add_arguments_from_option_loader(
    parser: argparse.ArgumentParser,
    option_loader: OptionLoader,
) -> argparse.ArgumentParser:
    # Set the config loader as a static variable on the action class so that it can be accessed from the action.
    ConfigOptionAction.option_loader = option_loader

    groups: dict[str, argparse._ArgumentGroup] = {}

    for cls in options.OPTION.__subclasses__():
        if cls.argument:
            group = cls.key.split(".")[0]
            if group not in groups:
                groups[group] = parser.add_argument_group(group)

            brief_doc = str(cls.__doc__).splitlines()[0]

            groups[group].add_argument(
                cls.argument,
                type=cls.data_type,
                default=cls.default,
                help=brief_doc,
                action=ConfigOptionAction,
                dest=cls.key,
            )

    return parser


def main() -> int:
    """Entry point for the 3lc CLI."""

    # Do not add help at this stage, as we want to add it later after having added the _Options subclasses.
    early_parser = create_parser(add_help=False)

    early_args, _ = early_parser.parse_known_args()

    verbosity_to_level_map = {0: "WARNING", 1: "INFO", 2: "DEBUG"}
    verbosity_log_level = verbosity_to_level_map.get(early_args.verbose, "DEBUG")

    # Bring up  logger for use by the configuration.
    # This is not the final 3LC "tlc" logger, but it is the first one we can use.
    logger = logging.getLogger("tlcconfig")
    logger.setLevel(verbosity_log_level)
    logger.addHandler(logging.StreamHandler())  # Default stream handler to stderr.

    # Create the initial config loader, loading the programmatic defaults
    option_loader = OptionLoader(initialize=False)

    config_file = OptionLoader.resolve_effective_config_file(early_args.config_file)  # arg has precedence

    if config_file:
        try:
            option_loader.update_from_yaml_file(config_file)
        except (ValueError, AttributeError) as e:
            error_message = f"Error loading config from {config_file}: {e}"
            logger.debug(error_message)
            print(error_message, file=sys.stderr)
            return -1
    elif config_file is None:
        logger.debug("No config file found -- using default values")
    else:
        logger.debug("Config file disabled -- using default values")

    option_loader.update_from_environment()
    OptionLoader.set_instance(option_loader, write_config_file=False)

    full_parser = create_parser()
    add_arguments_from_option_loader(full_parser, option_loader)

    # With the configuration loaded, we can now set up the logger.
    LoggerConfigurator.instance().enable_log_file()  # The object service should always log to file.

    subparsers = full_parser.add_subparsers(title="Sub-commands", dest="subcommand")

    # Add a pseudo-subparser for ExportSubCommand.
    # We do not want to fully initialize it at this stage, as it will import the tlc-module.

    # Set up the subcommands.
    sub_commands = {
        ConfigSubCommand.key: ConfigSubCommand(subparsers, option_loader),
        LoginSubCommand.key: LoginSubCommand(subparsers, option_loader),
        ObjectServiceSubCommand.key: ObjectServiceSubCommand(subparsers),
        ExportSubCommand.key: ExportSubCommand(subparsers),
    }

    args, _ = full_parser.parse_known_args()

    # If a valid config file is specified and it does not yet exist, write the current config to it.
    if config_file and not ("subcommand" in args and args.subcommand == ConfigSubCommand.key):
        option_loader.write_to_yaml_file(filename=config_file, overwrite=False)

    # Check if user has overridden the verbosity level on the command line. This check relies on
    # 0 being the default verbosity level.
    if early_args.verbose != 0:
        option_loader.set_value(options.LOGLEVEL, verbosity_log_level, ConfigSource.COMMAND_LINE)
        LoggerConfigurator.instance().set_log_level(verbosity_log_level)

    LoggerConfigurator.instance().initialize_logging_config()

    # The config subcommand is a bit special and does not touch the config file.
    # But, we need to handle it here to be able to print the final config.

    if "subcommand" in args and args.subcommand == ConfigSubCommand.key:
        return_value = sub_commands[ConfigSubCommand.key].handle_command(args)

    if "subcommand" in args and args.subcommand in sub_commands:
        sub_commands[args.subcommand].populate_effective_subparser()
        final_args = full_parser.parse_args()
        return_value = sub_commands[args.subcommand].handle_command(final_args)
    else:
        full_parser.print_help()
        return_value = 0

    return return_value


if __name__ == "__main__":
    sys.exit(main())
