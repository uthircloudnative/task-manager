from fastapi import FastAPI
from routers import task


app = FastAPI()

app.include_router(task.router, prefix="/api/v1", tags=["tasks"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True # Enable auto-reload for development purposes
    )