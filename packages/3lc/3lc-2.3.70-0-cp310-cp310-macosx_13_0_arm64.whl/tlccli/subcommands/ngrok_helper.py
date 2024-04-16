# =============================================================================
# <copyright>
# Copyright (c) 2024 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================

import importlib.util
import logging
import os
from typing import Optional


class NGrokHelper:
    """Class to setup NGrok for the service."""

    pyngrok_unavailable_message = (
        "NGrok is not available. You can install the package by running 'pip install 3lc[pyngrok]'."
    )

    ngrok_token_unavailable_message = "NGrok token could not be found. Please the set NGROK_TOKEN environment variable."

    def __init__(self, port: int) -> None:
        # Silence the pyngrok logger if it does not exist.
        # By checking for the existence of the logger, we avoid overwriting the level if it has already been set
        # in the global logging configuration.
        if "pyngrok" not in logging.Logger.manager.loggerDict:
            logging.getLogger("pyngrok").setLevel(logging.WARNING)

        from pyngrok import conf

        conf.get_default().auth_token = self.get_ngrok_token()
        self.port = port

    @staticmethod
    def is_pyngrok_available() -> bool:
        """Check if pyngrok module is available."""
        ngrok_spec = importlib.util.find_spec("pyngrok")
        return ngrok_spec is not None

    @staticmethod
    def is_ngrok_token_available() -> bool:
        """Check if the NGrok token is set."""
        return os.environ.get("NGROK_TOKEN") is not None

    @staticmethod
    def get_ngrok_token() -> Optional[str]:
        """Get the NGrok token."""
        if not os.environ.get("NGROK_TOKEN"):
            raise ValueError("NGrok token could not be found. Please set the NGROK_TOKEN environment variable.")
        else:
            return os.environ.get("NGROK_TOKEN")

    async def open_tunnel(self) -> None:
        """Open the NGrok tunnel.

        :returns: The public URL of the tunnel.
        """

        from pyngrok import ngrok

        # bind_tls = true opens only a https connection. See https://pyngrok.readthedocs.io/en/latest/api.html
        self.tunnel = ngrok.connect(self.port, bind_tls=True)

    async def close_tunnel(self) -> None:
        """Close the ngrok tunnel."""
        from pyngrok import ngrok

        ngrok.disconnect(self.tunnel)
