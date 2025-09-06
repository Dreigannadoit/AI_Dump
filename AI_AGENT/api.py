from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

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
    msg: str


@app.post("/chat")
def chat(request: ChatRequest):
    global state
    state["messages"].append({"role": "user", "content": request.msg})
    state = graph.invoke(state)
    reply =  state["messages"][-1].content
    return {"reply": reply}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=True)

