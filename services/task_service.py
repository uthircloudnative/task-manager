from datetime import date, datetime
from models.tasks import TaskList

from models.task import Task
from pathlib import Path
import csv

file_path = "data/task_data.csv"
file_path_obj = Path(file_path)
header_columns = ["id","title","description","category","status","completed_at","due_date","created_at"]

class TaskService:

    async def get_tasks(self, user_id: int, task_date: date):
        print("get_tasks Starts")
        # Logic to retrieve tasks for the user_id and task_date would go here
        task = Task(
            id=1,
            title="BUY_GROCERIES",
            description="This is task to buy groceries",
            category="HOME_TASK",
            status="Pending",
            completed_at=datetime.now(),
            due_date=task_date
        )
        tasks = TaskList(
            tasks=[task]
        )
        print("get_tasks Ends")
       
        return tasks
        
    async def create_task(self, user_id: int, task: Task):
        print("create_task Starts")
        try:
            task_data = {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "category": task.category,
                "status": task.status,
                "completed_at": task.completed_at,
                "due_date": task.due_date,
                "created_at": task.created_at
            }

            with file_path_obj.open("a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=header_columns)
                writer.writerow(task_data)
                print("Task created successfully")
        except Exception as e:
            print(f"Error creating task: {e}")
            raise e
        # Logic to create a task for the user_id would go here
        print("create_task Ends")
        return task