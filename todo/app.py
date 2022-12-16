from fastapi import FastAPI

from .routes import main_router


app = FastAPI(
    title="Todo",
    version="0.1.0",
    description="My first FASTAPI app, a simple todo app",
)

app.include_router(main_router)
