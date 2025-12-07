from datetime import date, datetime

class Task:
    def __init__(self, id: int, title: str, description: str, 
                 category: str, status: str, completed_at: datetime,
                 due_date: date=None, 
                 created_at: datetime=None):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.status = status
        self.completed_at = completed_at
        self.due_date = date.today()
        self.created_at = datetime.now()
    
    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}', due_date={self.due_date}, created_at={self.created_at}, completed_at={self.completed_at})"      