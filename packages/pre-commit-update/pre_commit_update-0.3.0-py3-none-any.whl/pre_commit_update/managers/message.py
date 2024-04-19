from typing import List, TypedDict

import click

from ..utils import get_color


class Message(TypedDict):
    message: str
    icon: str
    icon_alt: str
    text: str
    color: str


MessageType = List[Message]


class MessageManager:
    def __init__(self) -> None:
        self._to_update: MessageType = []
        self._no_update: MessageType = []
        self._excluded: MessageType = []
        self._kept: MessageType = []

    @property
    def to_update(self) -> MessageType:
        return self._to_update

    @property
    def no_update(self) -> MessageType:
        return self._no_update

    @property
    def excluded(self) -> MessageType:
        return self._excluded

    @property
    def kept(self) -> MessageType:
        return self._kept

    def add_to_update_message(
        self, name: str, current_version: str, latest_version: str
    ) -> None:
        to_update_message: str = (
            f"{name} - {get_color(current_version, 'yellow')} -> {get_color(latest_version, 'red')}"
        )
        self._to_update.append(
            Message(
                message=to_update_message,
                icon="✘",
                icon_alt="×",
                text="[outdated]",
                color="red",
            )
        )

    def add_no_update_message(self, name: str, version: str) -> None:
        no_update_message: str = f"{name} - {get_color(version, 'green')}"
        self._no_update.append(
            Message(
                message=no_update_message,
                icon="✔",
                icon_alt="√",
                text="[up-to-date]",
                color="green",
            )
        )

    def add_excluded_message(self, name: str, version: str) -> None:
        excluded_message: str = f"{name} - {get_color(version, 'magenta')}"
        self._excluded.append(
            Message(
                message=excluded_message,
                icon="★",
                icon_alt="*",
                text="[excluded]",
                color="magenta",
            )
        )

    def add_kept_message(
        self, name: str, current_version: str, latest_version: str
    ) -> None:
        text_message: str = (
            f"{current_version} -> {latest_version}"
            if current_version != latest_version
            else current_version
        )
        kept_message: str = f"{name} - {get_color(text_message, 'blue')}"
        self._kept.append(
            Message(
                message=kept_message,
                icon="◉",
                icon_alt="●",
                text="[kept]",
                color="blue",
            )
        )

    @staticmethod
    def output_messages(messages: MessageType) -> None:
        for message in messages:
            for symbol in (message["icon"], message["icon_alt"], message["text"]):
                try:
                    click.echo(
                        f"{message['message']} {get_color(click.style(symbol, bold=True), message['color'])}"
                    )
                    break
                except UnicodeEncodeError:
                    continue
