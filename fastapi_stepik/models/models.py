from pydantic import BaseModel


class User(BaseModel):
    name: str
    id: int


class User_age(BaseModel):
    name: str
    age: int


