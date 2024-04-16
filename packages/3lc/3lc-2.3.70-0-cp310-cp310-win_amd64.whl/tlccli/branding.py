# =============================================================================
# <copyright>
# Copyright (c) 2023 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================
"""Branding for 3LC CLI based on Rich."""

from __future__ import annotations

from typing import Any

import tlcconfig.options as options
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table
from tlcconfig.option_loader import OptionLoader


class _TLCBranding:
    """Branding for 3LC based on Rich.

    This class is used to generate the 3LC branding for the CLI and potentially other places.

    Ideally it should be moved to e.g. tlc.utils, but that would cause importing the tlc package before we are ready.
    """

    zest = "#F9F100"
    pearl = "#F0F0F0"
    neptune = "#2A6477"

    @staticmethod
    def color_str(str: str, color: str) -> str:
        """Return a string with the given color."""
        return f"[{color}]{str}[/{color}]"

    @staticmethod
    def abbrev(s0: str = "3", s1: str = "L", s2: str = "C.AI") -> str:
        """Return the 3LC abbreviation with the correct colors."""
        return (
            _TLCBranding.color_str(s0, _TLCBranding.zest)
            + _TLCBranding.color_str(s1, _TLCBranding.neptune)
            + _TLCBranding.color_str(s2, _TLCBranding.pearl)
        )


def format_config_table(option_loader: OptionLoader) -> Table:
    """Format the current configuration as a rich table."""

    table = Table(title="3LC Configuration")
    table.add_column("Key")
    table.add_column("Value")
    table.add_column("Source")

    for key, value in option_loader._option_values.items():
        if key.is_hidden():
            continue
        if key.key == "service.license":
            continue
        table.add_row(key.key, str(value.value), str(value.config_source.name))

    return table


def format_verbose_options_table(option_loader: OptionLoader) -> Table:
    table = Table(title="3LC Configuration")
    table.add_column("Key")
    table.add_column("Description", max_width=60)
    table.add_column("Default")

    for option in options.OPTION.__subclasses__():
        if option.is_hidden():
            continue
        help = str(option.__doc__)
        if option.envvar:
            help += f" (Environment variable: {option.envvar})"

        table.add_row(option.key, help, str(option.default))

    return table


def pretty_print(data: Any) -> None:
    console = Console()
    console.print(data)


def pretty_print_yaml(text: str) -> None:
    renderable = Syntax(text, "yaml", theme="ansi_dark")

    pretty_print(renderable)


def format_config_file(option_loader: OptionLoader) -> str:
    return (
        f"Effective config file: [link={option_loader.config_file}]{option_loader.config_file}[/link]"
        if option_loader.config_file
        else "Effective config file: Config file disabled."
    )
