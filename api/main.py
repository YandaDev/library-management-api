from fastapi import FastAPI
from . import crud, models

app = FastAPI()

@app.get("/members")
def list_members():
    return crud.get_all_members()

@app.post("/members")
def add_member(member: models.Member):
    return crud.create_member(member.name, member.email)
