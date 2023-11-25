from pydantic import BaseModel


class User(BaseModel):
    name: str
    id: int


class User_age(BaseModel):
    name: str
    age: int


class UserInfo(BaseModel):
    username: str
    user_info: str


class Feedback(BaseModel):
    name: str
    message: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

