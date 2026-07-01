from fastapi import FastAPI
from langchain_core import agents
from pydantic import BaseModel
from model import  Model

app = FastAPI()
agent = Model()

class Prompt(BaseModel):
    prompt:str

@app.post("/chat")
def chat(request:Prompt):
    answer = agent.answer_queries(request.prompt)

    return {
        "question": request.prompt,
        "answer": answer
    }