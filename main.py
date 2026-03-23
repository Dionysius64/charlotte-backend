from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import logging

from config import load_config
from state import messages
from state import add_message, get_messages_since
from llm.chat_llm import ChatLLM

logger = logging.getLogger("chat_app")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

config = load_config()
llm = ChatLLM(config)

# ------------------------
# HELPERS
# ------------------------

def trigger_llm_if_needed():

    if not messages:
        return

    last_msg = messages[-1]

    logger.info(f"Checking LLM trigger for message: {last_msg}")

    if last_msg["author"] == llm.name:
        logger.info("Last message already from LLM, skipping")
        return

    logger.info("Triggering LLM response...")

    reply = llm.generate_reply(messages)

    reply["timestamp"] = datetime.utcnow().isoformat()

    messages.append(reply)

    logger.info(f"LLM reply appended: {reply}")


# ------------------------
# ENDPOINTS
# ------------------------

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/send_message")
def send_message(msg: dict):

    logger.info(f"Incoming message: {msg}")

    stored = add_message(
        msg["author"],
        msg["message"],
        msg.get("emotion", 0),
    )

    trigger_llm_if_needed()

    return stored


@app.get("/messages")
def get_messages(last_timestamp: str | None = None):

    trigger_llm_if_needed()

    msgs = get_messages_since(last_timestamp)

    logger.info(f"Returning {len(msgs)} messages")

    return {"messages": msgs}