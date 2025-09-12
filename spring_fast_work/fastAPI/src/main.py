from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel

todo_data = {
    1 : {
        "id" : 1,
        "content": "FastAPI 색션 1 수강",
        "is_done": True
    },
    2 : {
        "id" : 2,
        "content": "FastAPI 색션 2 수강",
        "is_done": False
    },
    3 : {
        "id" : 3,
        "content": "FastAPI 색션 3 수강",
        "is_done": False
    },
}

app = FastAPI()

@app.get("/")
def hello_handler():
    return {"name":"cheon"}

@app.get("/todos")
def get_todos_handler(order: str | None = None): #order를 받거나 아무것도 입력되지 않거나.
    ret = list(todo_data.values())

    if order and order == "DESC": # order의 값이 있고, order가 "DESC"일때
        return ret[::-1]

    return ret

@app.get("/todos/{todo_id}", status_code=200)
def get_todo_handler(todo_id: int):
    todo = todo_data.get(todo_id)

    if todo:
        return todo
    
    raise HTTPException(status_code=404, detail="Todo Not Found") 

class CreateTodoRequest(BaseModel):
    id : int
    contents: str
    is_done: bool

@app.post("/todos")
def create_todo_handler(request: CreateTodoRequest):
    todo_data[request.id] = request.model_dump()
    return todo_data[request.id]

@app.patch("/todos/{todo_id}")
def update_todo_handler(todo_id: int, is_done: bool = Body(..., embed=True)): # is_done을 업데이트하기
    todo = todo_data.get(todo_id) #없을 경우 None을 반환

    if todo:
        todo['is_done'] = is_done
        return todo
    
    return {}

@app.delete("/todos/{todo_id}")
def delete_todo_handler(todo_id: int):
    todo_data.pop(todo_id, None)

    return todo_data