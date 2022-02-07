from pydantic import BaseModel, Field


class Todo(BaseModel):
    title: str = Field(title="The title of the todo", max_length=50
                       )
    description: str = Field(title="The description of the todo", max_length=200
                             )
