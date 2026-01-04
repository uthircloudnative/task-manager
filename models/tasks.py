from pydantic import BaseModel
from models.task import Task

class TaskList(BaseModel):
    tasks: list[Task]