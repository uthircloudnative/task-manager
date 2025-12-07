"""

"""

from fastapi import APIRouter, Depends
from datetime import date
from services.task_service import TaskService

router = APIRouter()

def get_task_service():
    return TaskService()


@router.get("/tasks/{user_id}")
async def get_tasks(user_id: int, task_date: date=date.today(), service: TaskService = Depends(get_task_service)):
    print("get_tasks Starts")
    task = await service.get_tasks(user_id, task_date)
    print("get_tasks Ends")
    return task
