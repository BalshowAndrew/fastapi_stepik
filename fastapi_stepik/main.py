from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

from models.models import User, User_age, UserInfo

app = FastAPI()


fake_db = [{"username": "vasya", "user_info": "любит колбасу"},
           {"username": "katya", "user_info": "любит петь"}]


@app.post("/")
async def root(user: User):
    print(f"У юзера {user.name} такой id: {user.id}")
    return user


@app.get("/users")
async def get_all_users():
    return fake_db


@app.post("/add_user", response_model=UserInfo) # тут указали модель (ормат) ответа
async def add_user(user: UserInfo): # тут проверяем входные данных на соответствие модели
    fake_db.append({"username": user.username, "user_info": user.user_info}) # тут добавили юзера в фейковую базу данных
    return user


@app.post("/user")
async def user_age(user: User_age):
    return{"name": user.name,
           "age": user.age,
           "is_adult": user.age >= 18}



@app.get("/index", response_class=FileResponse)
async def root_index():
    return FileResponse("fastapi_stepik/index.html")


@app.post("/calculate")
async def root_calculate(num1: int, num2: int):
    return {"result": f"{num1 + num2}"}


@app.get("/custom")
async def read_custom_message():
    return {"message": "This is a custom message!"}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
