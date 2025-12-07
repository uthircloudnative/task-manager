from datetime import date

from models.task import Task

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
            completed_at=None,
            due_date=task_date
        )
        print("get_tasks Ends")
        return [task]
        