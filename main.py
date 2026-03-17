from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

counter = 0
emotion = 0

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/conversation_title")
def get_title():
    return {"conversation_title": "Conversation"}

@app.get("/next_message")
def next_message():

    global counter
    counter += 1

    return {
        "message": f"{counter}",
        "author": "Backend"
    }

@app.get("/avatar")
def get_avatar():
    global counter
    return {"avatar_index": counter%7}