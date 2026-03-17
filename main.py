from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from state import add_message, get_messages_since

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- Models --------

class MessageIn(BaseModel):
    author: str
    message: str
    timestamp: str | None = None
    emotion: int = 0

# -------- Endpoints --------

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/send_message")
def send_message(msg: MessageIn):
    stored = add_message(msg.author, msg.message, msg.emotion)
    return stored


@app.get("/messages")
def get_messages(last_timestamp: str | None = None):
    msgs = get_messages_since(last_timestamp)
    return {"messages": msgs}