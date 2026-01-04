
from fastapi import APIRouter, Depends
from datetime import date
from services.task_service import TaskService
from models.task import Task

router = APIRouter()

# Create a single instance of TaskService
task_service = TaskService()

def get_task_service():
    return task_service


@router.get("/tasks/{user_id}")
async def get_tasks(user_id: int, task_date: date=date.today(), service: TaskService = Depends(get_task_service)):
    print("get_tasks Starts")
    tasks = await service.get_tasks(user_id, task_date)
    print("get_tasks Ends")
    return tasks

@router.post("/tasks/{user_id}")
async def create_task(user_id: int, task: Task, service: TaskService = Depends(get_task_service)):
    print("create_task Starts")
    task = await service.create_task(user_id, task)
    print("create_task Ends")
    return task
