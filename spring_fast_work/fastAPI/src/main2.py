from fastapi import FastAPI, Body, HTTPException
from chatbot_graph import graph
from pydantic import BaseModel

class PreferenceInput(BaseModel):
    preference: str

app = FastAPI()

@app.get("/hello")
def hello():
    return "hello from FastAPI"

@app.post("/run-graph")
def run_graph(input_data: PreferenceInput):
    init_state = {"user_preference":input_data.preference}
    res = graph.invoke(init_state)

    return res

@app.get("/run-graph")
def run_graph(preference: str):
    init_state = {"user_preference" : preference}
    res = graph.invoke(init_state)

    return res