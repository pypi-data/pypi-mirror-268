# =============================================================================
# <copyright>
# Copyright (c) 2023 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================
from __future__ import annotations

import argparse
from gettext import gettext

from tlccli.subcommand import SubCommand


class ExportSubCommand(SubCommand):
    """Handle the export sub-command."""

    key = "export"
    help = """The export sub-command allows exporting a table to a file.

            E.g. "3lc export path/to/table.json path/to/output.csv --format csv" will export the table at
            path/to/table.json to a CSV file at path/to/output.csv.

            Run with `export --help` for more details."""

    def __init__(
        self,
        subparsers: argparse._SubParsersAction[argparse.ArgumentParser],
    ):
        super().__init__(ExportSubCommand.key, subparsers)

        self.parser = subparsers.add_parser(
            ExportSubCommand.key,
            help=ExportSubCommand.help,
            add_help=False,  # Disable help to avoid printing the incomplete
            #  help message when the arguments are parsed for the first time.
        )

    def populate_effective_subparser(self) -> None:
        # We need to add the help manually since we disabled it above.
        # This code is a duplicate of how it is done by default in argparse when passing add_help=False
        # constructor above.
        self.parser.add_argument(
            "-h",
            "--help",
            action="help",
            default=argparse.SUPPRESS,
            help=gettext("show this help message and exit"),
        )

        self.parser.add_argument(
            "table-path",
            help="The path to the table to export.",
            type=str,
        )

        self.parser.add_argument(
            "output-path",
            help="The path to the exported output file.",
            type=str,
        )

        from tlc.core.export.exporter import Exporter

        self.parser.add_argument(
            "--format",
            help=(
                "The format of the output file."
                " Will be inferred from table content and output-path extension if not specified."
            ),
            dest="format",
            type=str,
            choices=list(Exporter.exporters.keys()),
        )

        Exporter.add_registered_exporters_to_parser(self.parser)

    def handle_command(self, args: argparse.Namespace) -> int:
        from tlc.core import Table, Url

        # Filter out kwargs which are not relevant for exporters
        export_args = [
            action.dest
            for action in self.parser._actions
            if isinstance(action, (argparse._StoreAction, argparse._StoreConstAction))
        ]
        kwargs = {k: v for k, v in vars(args).items() if k in export_args and v is not None}

        table = Table.from_url(Url(kwargs["table-path"]))
        output_url = Url(kwargs["output-path"])

        kwargs.pop("table-path")
        kwargs.pop("output-path")

        table.export(output_url, **kwargs)

        return 0
