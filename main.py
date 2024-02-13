from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import init_db, engine
from models import User
import crud


app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init_db()


@app.get("/get-users")
async def get_users() -> list[User]:
    return crud.get_all_users(engine)

@app.post("/create-user")
async def create_user(user: User):
    return crud.create_new_user(engine, user)
