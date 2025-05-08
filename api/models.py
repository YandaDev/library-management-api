from pydantic import BaseModel

class Member(BaseModel):
    name: str
    email: str

class Book(BaseModel):
    title: str
    author: str

class Borrow(BaseModel):
    member_id: int
    book_id: int
