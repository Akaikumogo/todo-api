from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False

todos = [
]
@app.get("/")
async def get():
    return "OPPO NIGGA"
@app.get("/todos")
async def get_todos():
    return todos

@app.post("/todos")
async def create_todo(todo_item: TodoItem):
    todos.append(todo_item)
    return todo_item

@app.put("/todos/{id}")
async def update_todo(id: int, todo_item: TodoItem):
    for todo in todos:
        if todo.id == id:
            todo.title = todo_item.title
            todo.completed = todo_item.completed
            return todo

@app.delete("/todos/{id}")
async def delete_todo(id: int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {"message": "Todo item deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
