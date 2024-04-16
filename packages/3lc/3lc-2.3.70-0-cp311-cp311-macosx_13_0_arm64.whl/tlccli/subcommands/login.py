# =============================================================================
# <copyright>
# Copyright (c) 2024 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================
"""Sub-command for the login command."""

from __future__ import annotations

import argparse

import tlcsaas
from tlcconfig import options
from tlcconfig.logger_configurator import LoggerConfigurator
from tlcconfig.option_loader import ConfigSource, OptionLoader

from tlccli.subcommand import SubCommand


class LoginSubCommand(SubCommand):
    """Handle the login sub-command."""

    key = "login"

    def __init__(
        self,
        subparser: argparse._SubParsersAction[argparse.ArgumentParser],
        option_loader: OptionLoader,
    ):
        self.option_loader = option_loader
        super().__init__(LoginSubCommand.key, subparser)
        self.parser = self.create_subparser(self.subparsers)

    def create_subparser(
        self,
        subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
    ) -> argparse.ArgumentParser:
        login_parser = subparsers.add_parser(
            self.name,
            help="""The login sub-command allows logging into 3LC.
            Run with `login --help` for more details.""",
        )

        login_parser.add_argument(
            "api_key",
            help="""The API key to use. If provided, the API key will be verified with 3LC (unless --no-verify is set)
            "and then saved to the API key file. If not provided, the command will search for an existing API key
            "and verify that (unless --no-verify is set). If not provided and no existing API key is found, the
            "system will prompt for the API key.""",
            type=str,
            default="",
            nargs="?",
        )

        login_parser.add_argument(
            "--no-verify",
            help="Do not verify the API key with 3LC.",
            action="store_true",
            default=False,
        )

        return login_parser

    def handle_command(self, args: argparse.Namespace) -> int:
        assert "api_key" in args
        orig_verbosity_log_level = OptionLoader.instance().get_value(options.LOGLEVEL)
        if args.verbose == 0:
            # Make sure verbosity is at least INFO for login command
            OptionLoader.instance().set_value(options.LOGLEVEL, "INFO", ConfigSource.COMMAND_LINE)
            LoggerConfigurator.instance().set_log_level("INFO")
            LoggerConfigurator.instance().initialize_logging_config(force=True)
        return_value = 0 if tlcsaas.login(args.api_key, args.no_verify) else 1
        if args.verbose == 0:
            # Restore verbosity level
            OptionLoader.instance().set_value(options.LOGLEVEL, orig_verbosity_log_level)
            LoggerConfigurator.instance().set_log_level(orig_verbosity_log_level)
            LoggerConfigurator.instance().initialize_logging_config(force=True)
        return return_value
