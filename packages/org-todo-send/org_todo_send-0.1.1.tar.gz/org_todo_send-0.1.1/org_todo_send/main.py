#!/usr/bin/env python3
from pysignalclirestapi import SignalCliRestApi  # type: ignore
from org_todo_send import parse  # type: ignore
import typer  # type: ignore
from typing_extensions import Annotated
import tomllib

app = typer.Typer()


@app.command()
def org_todo_send(
    org_file: Annotated[str, typer.Argument(help="Path to your Org file")],
    sender: Annotated[
        str,
        typer.Argument(
            envvar="SIGNAL_SENDER", help="The Signal phone number you are sending from."
        ),
    ],
    recipients_file: Annotated[
        str,
        typer.Argument(
            help="Path to a TOML file containing phone numbers or IDs of recipients."
        ),
    ],
    api_url: Annotated[
        str, typer.Argument(envvar="SIGNAL_API", help="URL of your Signal REST API.")
    ] = "http://localhost:8080",
    message_title: Annotated[str, typer.Option(help="Title of the message")] = "TODOs",
    html: Annotated[
        bool, typer.Option(help="Attach an HTML export of the Org file in the message.")
    ] = False,
):
    """Sends a message to recipients with their TODOs from an Org file. The TODO nodes in the Org file should be tagged with the recipient's name. Ex: @alice"""
    signal = SignalCliRestApi(base_url=api_url, number=sender)
    with open(recipients_file, "rb") as f:
        recipients = tomllib.load(f)

    attachments = [parse.org_to_html(org_file)] if html else None
    todos = parse.get_todos_from_org(org_file)

    # filter out recipients without todos
    recipients_trimmed = [
        (recipient, number)
        for recipient, number in recipients.items()
        if recipient in set(todos["people"].sum())
    ]

    for recipient, number in recipients_trimmed:
        message = parse.format_message(message_title, recipient, todos)
        signal.send_message(
            message=message, recipients=[number], attachments_as_bytes=attachments
        )
