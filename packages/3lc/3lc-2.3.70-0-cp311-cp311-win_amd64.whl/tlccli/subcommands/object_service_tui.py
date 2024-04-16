# =============================================================================
# <copyright>
# Copyright (c) 2024 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================

from __future__ import annotations

import asyncio
import logging
import os
from enum import Enum
from typing import Any

import pyclip
import rich.table
import rich.text
import uvicorn
from rich.logging import RichHandler
from rich.style import Style
from rich.table import Table
from starlite import Starlite
from textual.app import App, ComposeResult
from textual.containers import Center, Container, Horizontal, VerticalScroll
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button, Footer, Header, Label, RichLog, Static, Tree
from textual.worker import Worker, WorkerState
from tlcconfig.logger_configurator import LoggerConfigurator
from tlcconfig.version import _PACKAGE_VERSION

import tlccli.subcommands.object_service


class TextualLogHandler(logging.Handler):
    """
    A custom logging handler that outputs to a Textual Log widget.
    """

    def __init__(self, log_widget: RichLog):
        super().__init__()
        self.log_widget = log_widget
        self.rich_handler = RichHandler(markup=True)

    def emit(self, record: Any) -> None:
        """
        Override the emit method to forward log records to the Textual Log widget.

        :param record: The log record to emit.
        """
        # Format the record and send it to the Textual Log widget
        message = self.format(record)

        rendered_message = self.rich_handler.render_message(record, message)
        self.log_widget.write(rendered_message)


class LoggingFormatter(logging.Formatter):
    def formatMessage(self, record: logging.LogRecord) -> str:
        log = super().formatMessage(record)
        return log


def _get_current_log_level_name() -> str:
    return logging.getLevelName(logging.getLogger("tlc").getEffectiveLevel())


def _get_user_name() -> str:
    from tlcsaas.api_key import ApiKey

    apikey = ApiKey.instance()
    ret = apikey.user_info.user_full_name
    if len(ret) > 0:
        ret += " - "
    return ret + apikey.user_info.user_email


def _get_tenant_name() -> str:
    from tlcsaas.api_key import ApiKey

    apikey = ApiKey.instance()
    return apikey.user_info.tenant_name


def _get_config_file_path() -> str:
    from tlcconfig.option_loader import OptionLoader

    config_file = OptionLoader.resolve_effective_config_file()
    if config_file is None:
        return ""
    return config_file


class ObjectServiceStatus(Enum):
    NONE = "None"
    STARTING = "[bright_yellow]Starting[/bright_yellow]"
    RUNNING = "[bright_green]Running[/bright_green]"
    STOPPING = "[bright_yellow]Stopping[/bright_yellow]"
    STOPPED = "Stopped"
    ERROR = "[red]Error[/red]"


class DynamicInformation(Widget):
    """Widget which contains dynamic information about the application."""

    user_name = reactive("")
    tenant_name = reactive("")
    config_file_path = reactive("")
    log_level_name = reactive("")
    log_file_path = reactive("")
    status_message = reactive(ObjectServiceStatus.NONE)
    dashboard_urls: reactive[list[str]] = reactive([])
    object_service_urls: reactive[list[str]] = reactive([])

    def __init__(self) -> None:
        super().__init__()
        self.set_reactive(
            DynamicInformation.log_file_path,
            LoggerConfigurator.instance().get_current_log_file_path(),
        )
        self.set_reactive(DynamicInformation.log_level_name, _get_current_log_level_name())
        self.set_reactive(DynamicInformation.config_file_path, _get_config_file_path())

        self.table_os = Static(id="table_os_static")
        self.table_tlc = Static(id="table_tlc_static")

        self.create_url_tree()

    def create_label_with_copy_button(self, label: str = "", id: str = "") -> Horizontal:
        return Horizontal(
            Label(label, id=id),
            Button(":clipboard:", classes="copy_button", id=f"{id}_button"),
            id=f"{id}_container",
            classes="copy_container",
        )

    def create_url_tree(self) -> None:
        tree: Tree[dict] = Tree("URLs (Click to copy to clipboard)")
        tree.show_root = False
        tree.root.expand()
        self.dashboard_urls_node = tree.root.add("Dashboard URLs")
        self.object_service_urls_node = tree.root.add("Object Service URLs")

        self.url_tree = tree

    def format_rich_tables(self) -> tuple[rich.table.Table, rich.table.Table]:
        title_style = Style(color="#F0F0F0", bold=True)  # This is the bone color from the 3LC Style Guide

        os_table = Table(show_header=False, box=None, title="System", title_style=title_style, min_width=30)
        os_table.add_column(min_width=10, max_width=10)
        os_table.add_column(justify="left")

        os_table.add_row("[label]User", f"{self.user_name}")
        os_table.add_row("[label]Workspace", f"{self.tenant_name}")
        os_table.add_row("[label]Status[/label]", f"{self.status_message.value}")

        tlc_table = Table(show_header=False, box=None, title="Config", title_style=title_style)
        tlc_table.add_column()
        tlc_table.add_column()

        tlc_table.add_row("[label]Config File", f"[link]{self.config_file_path}[/link]")
        tlc_table.add_row("[label]Log File", f"[link]{self.log_file_path}[/link]")
        tlc_table.add_row("[label]Log Level", f"{self.log_level_name}")

        return os_table, tlc_table

    def compose(self) -> ComposeResult:
        metadata = VerticalScroll(
            Container(
                Center(
                    self.table_os,
                    self.table_tlc,
                ),
                classes="dynamic_information_container dashboard",
            ),
            Container(
                self.url_tree,
                id="url_tree",
            ),
        )
        yield metadata

    def do_update(self) -> None:
        os_table, tlc_table = self.format_rich_tables()
        self.table_os.update(os_table)
        self.table_tlc.update(tlc_table)

    def watch_user_name(self, value: str) -> None:
        """Called when user_name changes."""
        self.do_update()

    def watch_tenant_name(self, value: str) -> None:
        """Called when tenant_name changes."""
        self.do_update()

    def watch_config_file_path(self, value: str) -> None:
        """Called when config_file_path changes."""
        self.do_update()

    def watch_log_level_name(self, value: str) -> None:
        """Called when log_level_name changes."""
        self.do_update()

    def watch_log_file_path(self, value: str) -> None:
        """Called when log_file_path changes."""
        self.do_update()

    def watch_status_message(self, value: str) -> None:
        self.do_update()

    def watch_dashboard_urls(self, value: list[str]) -> None:
        self.dashboard_urls_node.remove_children()
        for url in value:
            self.dashboard_urls_node.add_leaf(f"[link]{url}[/link]")

        self.dashboard_urls_node.expand()

    def watch_object_service_urls(self, value: list[str]) -> None:
        self.object_service_urls_node.remove_children()
        for url in value:
            self.object_service_urls_node.add_leaf(f"[link]{url}[/link]")

        self.object_service_urls_node.expand()

    def on_tree_node_selected(self, event: Tree.NodeSelected[dict]) -> None:
        if isinstance(event.node.label, rich.text.Text):
            url = event.node.label.plain
            pyclip.copy(url)
        elif isinstance(event.node.label, str):
            url = event.node.label
            pyclip.copy(url)

    @staticmethod
    def format_user_name(value: str) -> str:
        return f"User: {value}"

    @staticmethod
    def format_tenant_name(value: str) -> str:
        return f"Workspace: {value}"

    @staticmethod
    def format_config_file_path(value: str) -> str:
        return f"Config File: [link={value}]{value}[/link]"

    @staticmethod
    def format_log_file(value: str) -> str:
        return f"Log File: [link={value}]{value}[/link]"

    @staticmethod
    def format_log_level(value: str) -> str:
        return f"Log Level: {value}"


class ObjectServiceTUI(App):
    """A full screen text application for running the 3LC Object Service in a terminal."""

    CSS_PATH = "object_service_tui.tcss"

    BINDINGS = [
        ("q", "quit", "Shut down and exit"),
        ("l", "log_level_toggle", "Toggle log level"),
    ]

    def __init__(self, host: str, port: int, ngrok: bool, public_examples: bool) -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.ngrok = ngrok
        self.public_examples = public_examples
        self.object_service_worker: Worker | None = None
        self.import_tlc_worker: Worker | None = None

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True, id="header")

        with Container(id="main_container"):
            # Dynamic Information
            self.dynamic_information = Container(DynamicInformation(), id="dynamic_information")
            yield self.dynamic_information

            # Log Widget
            self.log_widget = RichLog(id="log", max_lines=1000)
            self.log_widget.border_title = "Log"
            handler = TextualLogHandler(self.log_widget)
            handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

            # Remove the default stream handler which prints to stdout.
            stream_handler = next(
                (h for h in logging.getLogger("tlc").handlers if h.name == "tlc_stream_handler"), None
            )
            if stream_handler:
                logging.getLogger("tlc").removeHandler(stream_handler)

            logging.getLogger("tlc").addHandler(handler)

            # Remove stdout handler if it is present
            yield Container(self.log_widget, id="log_widget_container")

        yield Footer()

    async def on_mount(self) -> None:
        self.title = "3LC Object Service"
        self.sub_title = f"version: {_PACKAGE_VERSION} PID: {os.getpid()}"

    def on_worker_state_changed(self, event: Worker.StateChanged) -> None:
        if event.worker == self.import_tlc_worker:
            if event.state == WorkerState.SUCCESS:
                self.post_message(self.TLCImportedMessage())

            if event.state == WorkerState.ERROR:
                self.post_message(self.TLCImportFailedMessage(str(event.worker.error)))
                pass

        if event.worker == self.object_service_worker:
            if event.state == WorkerState.CANCELLED or event.state == WorkerState.SUCCESS:
                self.exit()

    class TLCImportedMessage(Message):
        def __init__(self) -> None:
            super().__init__()

    def on_object_service_tui_tlcimported_message(self, message: TLCImportedMessage) -> None:
        self.object_service_worker = self.run_worker(self.serve_object_service())
        pass

    class TLCImportFailedMessage(Message):
        def __init__(self, error_message: str) -> None:
            super().__init__()
            self.error_message = error_message

    def on_object_service_tui_tlcimport_failed_message(self, message: TLCImportFailedMessage) -> None:
        self.notify(f"Failed to import tlc: {message.error_message}", title="Object Service", severity="error")
        self.query_one(DynamicInformation).status_message = ObjectServiceStatus.ERROR
        pass

    class ObjectServiceStartedMessage(Message):
        def __init__(self) -> None:
            super().__init__()

    def on_object_service_tui_object_service_started_message(self, message: ObjectServiceStartedMessage) -> None:
        self.notify("Object Service Started", title="Object Service")
        self.query_one(DynamicInformation).status_message = ObjectServiceStatus.RUNNING
        self.query_one(DynamicInformation).user_name = _get_user_name()
        self.query_one(DynamicInformation).tenant_name = _get_tenant_name()
        pass

    def on_ready(self) -> None:
        self.notify("Starting Object Service...", title="Object Service")
        # To avoid blocking the UI (too much) we start the import_tlc worker in a separate thread.
        # When tlc is imported, the Object Service will be started as a coroutine from the main thread.
        self.query_one(DynamicInformation).status_message = ObjectServiceStatus.STARTING
        self.import_tlc_worker = self.run_worker(self.import_tlc(), thread=True, exit_on_error=False)

    async def action_quit(self) -> None:
        if self.object_service_worker:
            self.notify("Shutting down Object Service...", title="Object Service")
            self.query_one(DynamicInformation).status_message = ObjectServiceStatus.STOPPING
            self.object_service_worker.cancel()
            # The actual call to quit() is handled in on_worker_state_changed
        else:
            self.exit()

    def action_log_level_toggle(self) -> None:
        current_log_level = _get_current_log_level_name()
        next_log_level = LoggerConfigurator.get_next_log_level(current_log_level)
        logging.getLogger("tlc").setLevel(next_log_level)
        logging.getLogger("tlc").info(f"Changing log level from {current_log_level} to {next_log_level}")
        self.query_one(DynamicInformation).log_level_name = next_log_level
        pass

    def object_service_shutdown_handler(self, starlite: Starlite) -> None:
        """Handler that will be passed to Starlite and called when the object service has shut down..

        This handler will also be invoked if startup fails.

        """
        pass

    def after_object_service_startup_handler(self, starlite: Starlite) -> None:
        """Handler that will be passed to Starlite and called when the object service is running.

        This handler will be invoked from the thread of the object service.

        """
        from tlc.service.object_service import StarliteStateConstants

        self.query_one(DynamicInformation).object_service_urls = starlite.state[
            StarliteStateConstants.OBJECT_SERVICE_RUNNING_URLS
        ]

        self.query_one(
            DynamicInformation
        ).dashboard_urls = tlccli.subcommands.object_service.get_effective_dashboard_urls(starlite.state)

        self.post_message(self.ObjectServiceStartedMessage())

    async def import_tlc(self) -> None:
        """Import tlc to ensure that the global objects are created."""
        try:
            import tlc  # noqa: F401
        except Exception as e:
            logging.getLogger("tlc").error(f"Failed to import tlc: {e}")
            raise e

    async def serve_object_service(self) -> None:
        from tlc.service import object_service  # noqa: I001

        if self.public_examples:
            tlccli.subcommands.object_service.configure_public_examples()

        app = object_service.create_starlite_app(
            self.host,
            self.port,
            self.ngrok,
            self.after_object_service_startup_handler,
            self.object_service_shutdown_handler,
        )

        config = uvicorn.Config(
            app,
            port=self.port,
            host=self.host,
            log_level="warning",
            timeout_keep_alive=60,
        )

        self.uvicorn_server = uvicorn.Server(config)
        try:
            await self.uvicorn_server.serve()
        except asyncio.CancelledError:
            await self.uvicorn_server.shutdown()
        except Exception:
            pass

        pass
