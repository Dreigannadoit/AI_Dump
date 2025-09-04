import os
import json
from typing import TypedDict

from dotenv import load_dotenv
from imap_client import IMAPClient

from imap_tools import MailBox, AND

from langchain.chat_models import init_chat_model
from langchain_core.tools import tool

from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, START, END

load_dotenv()

IMAP_HOST = os.getenv("IMAP_HOST")
IMAP_PORT = os.getenv("IMAP_PORT")
IMAP_USER = os.getenv("IMAP_USER")
IMAP_PASSWORD = os.getenv("IMAP_PASSWORD")
IMAP_FOLDER = 'INBOX'

CHAT_MODEL = "qwen3:8b"

class ChatState(TypedDict):
    messages: list


def connect():
    mail_box = MailBox(IMAP_HOST)
    mail_box.login(IMAP_USER, IMAP_PASSWORD, initial_folder=IMAP_FOLDER)

    return mail_box


@tool
def list_unread_emails():
    """Return a bullet list of every UNREAD message's UID, subject date and sender """

    print("List Unread Email Tool Called")

    with connect() as mb:
        unread = list(mb.fetch(criteria = AND(seen=False), headers_only=True, mark_seen=False))

    if not unread:
        return "You have no unread messages"

    response = json.dumps([
        {
            'uid': mail.uid,
            'date': mail.date.astimezone().strftime('%Y-%m-%d %H:%M'),
            'subject': mail.subject,
            'sender': mail.from_,

        } for mail in unread
    ])

    return response


@tool
def summarize_email(uid):
    """Summarize a single e-mail given its IMAP UID. Return a short summary of the e-mail content / body in plain text."""

    print("Summarize Email Tool Called", uid)

    with connect() as mb:
        mail = next(mb.fetch(AND(uid=uid), mark_seen=False), None)

        if not mail:
            return f'Could not summarize email with UID {uid}'

        prompt = (
            "Summarize this e-mail concisely: \n\n"
                f"Subject: {mail.subject}\n"
                f"Sender: {mail.from_}\n"
                f"Date: {mail.date}\n\n"
                f"{mail.text or mail.html}\n"
        )

        return raw_llm.invoke(prompt).content


llm = init_chat_model(CHAT_MODEL, model_provider='ollama')
llm = llm.bind_tools([list_unread_emails, summarize_email])

raw_llm =init_chat_model(CHAT_MODEL, model_provider='ollama')


