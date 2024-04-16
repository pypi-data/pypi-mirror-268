# =============================================================================
# <copyright>
# Copyright (c) 2023 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================
"""Sub-command for the config command."""

from __future__ import annotations

import argparse

from tlcconfig.option_loader import OptionLoader

import tlccli.branding as branding
from tlccli.subcommand import SubCommand


class ConfigSubCommand(SubCommand):
    """Handle the config sub-command."""

    key = "config"

    def __init__(
        self,
        subparser: argparse._SubParsersAction[argparse.ArgumentParser],
        option_loader: OptionLoader,
    ):
        self.option_loader = option_loader
        super().__init__(ConfigSubCommand.key, subparser)
        self.parser = self.create_subparser(self.subparsers)

    def create_subparser(
        self,
        subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
    ) -> argparse.ArgumentParser:
        config_parser = subparsers.add_parser(
            self.name,
            help="""The config sub-command allows inspecting the configuration.
            Run with `config --help` for more details.""",
        )
        config_parser.add_argument(
            "--list",
            help="""List the configuration that will be resolved by the current combination of configuration files,
            environment variables and command-line options and exit.""",
            action="store_true",
            dest="config_list",
        )

        config_parser.add_argument(
            "--describe",
            help="Describe the configuration options and exit.",
            action="store_true",
            dest="config_describe",
        )

        config_parser.add_argument(
            "--to-yaml",
            help="Print the current configuration in YAML format and exit.",
            action="store_true",
            dest="config_to_yaml",
        )

        return config_parser

    def handle_command(self, args: argparse.Namespace) -> int:
        if "config_list" in args and args.config_list:
            branding.pretty_print(branding.format_config_table(self.option_loader))
            branding.pretty_print(branding.format_config_file(self.option_loader))
            return 0

        if "config_describe" in args and args.config_describe:
            branding.pretty_print(branding.format_verbose_options_table(self.option_loader))
            return 0

        if "config_to_yaml" in args and args.config_to_yaml:
            branding.pretty_print_yaml(self.option_loader.to_yaml())
            return 0

        # If config command is invoked, without any argument, print its help and exit.|
        if "subcommand" in args and args.subcommand == "config":
            self.parser.print_help()
            return 0

        return 0
