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
from abc import ABC, abstractmethod


class SubCommand(ABC):
    """Base class for sub-commands used by 3LC CLI"""

    def __init__(
        self,
        name: str,
        subparser: argparse._SubParsersAction[argparse.ArgumentParser],
    ):
        self.name = name
        self.subparsers = subparser

    @abstractmethod
    def handle_command(self, args: argparse.Namespace) -> int:
        """Handle a command that has been determined to be for this sub-command."""
        pass

    def populate_effective_subparser(self) -> None:
        """Create the subparser for this sub-command.

        This method will be called once we have determined that there is a command for this sub-command. This allows us
        to delay importing tlc until we know we need it.
        """
        pass
