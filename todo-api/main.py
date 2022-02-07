from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import (fetch_one_todo, fetch_all_todos,
                      create_todo, update_todo, remove_todo)
from model import Todo


app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/")
def read_root():
    return {"ping": "pong"}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo item with this title {title}")


@app.post("/api/todo")
async def post_todo(new_todo: Todo):
    response = await create_todo(new_todo.dict())
    if response:
        return "New todo is successfully created"
    raise HTTPException(400, "Something went wrong / Bad Request")


@app.put("/api/todo/{title}")
async def put_todo(title: str, updateData: Todo):
    response = await update_todo(title, updateData.dict())
    if response:
        return "Successfully updated todo item !"
    raise HTTPException(404, f"There is no todo item with this title {title}")


@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo item !"
    raise HTTPException(404, f"There is no todo item with this title {title}")
