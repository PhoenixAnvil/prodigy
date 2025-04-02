from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Prodigy",
    description="Microservice API to manage software products for a software development shop",
)

app.include_router(router)
