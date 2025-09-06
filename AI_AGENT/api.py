from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import re

from main import graph
state = {"messages": []}

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    global state
    state["messages"].append({"role": "user", "content": request.message})
    state = graph.invoke(state)
    raw_reply = state["messages"][-1].content

    think_match = re.search(r"<think>(.*?)</think>", raw_reply, re.DOTALL)
    think_text = think_match.group(1).strip() if think_match else None

    visible_reply = re.sub(r"<think>.*?</think>", "", raw_reply, flags=re.DOTALL).strip()

    return {"reply": visible_reply, "think": think_text}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

