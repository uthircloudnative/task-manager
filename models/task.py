from pydantic import BaseModel
from datetime import date, datetime

class Task(BaseModel):
    # def __init__(self, id: int, title: str, description: str, 
    #              category: str, status: str, completed_at: datetime,
    #              due_date: date=None, 
    #              created_at: datetime=None):
        id: int
        title: str
        description: str
        category: str
        status: str
        completed_at: datetime = datetime.now()
        due_date: date
        created_at: datetime = datetime.now()
    
        def __repr__(self):
            return f"Task(id={self.id}, title='{self.title}', status='{self.status}', due_date={self.due_date}, created_at={self.created_at}, completed_at={self.completed_at})"      