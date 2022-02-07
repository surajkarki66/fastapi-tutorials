import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection, AsyncIOMotorDatabase
from model import Todo


client = AsyncIOMotorClient(
    "mongodb://localhost:27017")

database = AsyncIOMotorDatabase(client, name="todo")
collection = AsyncIOMotorCollection(database, name="todos")


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    if result.acknowledged:
        return True
    return False


async def update_todo(title, updatedTodo):
    await collection.update_one({"title": title}, {"$set": {"title": updatedTodo["title"], "description": updatedTodo["description"]}})
    return True


async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True
