#!/usr/bin/env python3
import orgparse  # type: ignore
import pandas as pd
import pypandoc  # type: ignore
from datetime import datetime


def get_todos_from_org(org_file: str) -> pd.DataFrame:
    """
    Extracts todos from an Org file using orgparse and returns a list of Todos.
    """
    org = orgparse.load(org_file)
    todo_nodes = [n for n in org[1:] if n.todo == "TODO"]

    todos_dict: dict = {
        "text": [],
        "people": [],
        "priority": [],
        "body": [],
        "tags": [],
        "deadline": [],
        "scheduled": [],
        "parent": [],
    }

    for node in todo_nodes:
        todos_dict["text"].append(node.heading)
        todos_dict["people"].append(
            [t[1:].lower() for t in node.shallow_tags if "@" in t]
        )
        todos_dict["priority"].append(node.priority)
        todos_dict["body"].append(node.body)
        todos_dict["tags"].append(node.shallow_tags)
        todos_dict["deadline"].append(
            None
            if node.deadline.start is None
            else datetime.strptime(str(node.deadline), "<%Y-%m-%d %a>")
        )
        todos_dict["scheduled"].append(
            None
            if node.scheduled.start is None
            else datetime.strptime(str(node.scheduled), "<%Y-%m-%d %a>")
        )
        todos_dict["parent"].append(node.parent.heading)

    todos_df = pd.DataFrame(todos_dict)

    return todos_df


def format_message(title: str, recipient_name: str, todos: pd.DataFrame) -> str:
    boolean_mask = [recipient_name in lst for lst in todos["people"]]
    df = todos[boolean_mask]
    ret = f"{title}\n\n"

    for parent in df["parent"].unique():
        parent_df = df[df["parent"] == parent]

        ret += f"{parent}\n"

        for task in parent_df["text"]:
            ret += f"- {task}\n"

        ret += "\n"

    return ret


def org_to_html(org_file: str) -> str:
    with open(org_file, "r") as f:
        org = f.read()

    html = pypandoc.convert_text(
        org, "html", format="org", extra_args=["-s", "--toc", "--toc-depth=2"]
    )
    return html.encode("utf-8")
