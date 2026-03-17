from datetime import datetime

messages = []

def add_message(author: str, message: str, emotion: int):
    timestamp = datetime.utcnow().isoformat()

    msg = {
        "author": author,
        "message": message,
        "timestamp": timestamp,
        "emotion": emotion,
    }

    messages.append(msg)
    return msg


def get_messages_since(last_timestamp: str | None):
    if not last_timestamp:
        return messages

    return [
        m for m in messages
        if m["timestamp"] > last_timestamp
    ]