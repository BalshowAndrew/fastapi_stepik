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



