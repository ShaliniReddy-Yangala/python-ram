from fastapi import FastAPI
from app.database import engine, Base
from app.routers import users

Base.metadata.create_all(bind=engine)  # creates tables

app = FastAPI()

app.include_router(users.router)
