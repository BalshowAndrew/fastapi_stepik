from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import json
from pathlib import Path

from models.models import User, User_age, UserInfo, Feedback



app = FastAPI()


fake_db = [{"username": "vasya", "user_info": "любит колбасу"},
           {"username": "katya", "user_info": "любит петь"}]

fake_users = {
    1: {"username": "john_doe", "email": "jong@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
    3: {"username": "ivan_fitch", "email": "ivan@example.com"},
    4: {"username": "johan_black", "email": "johan@example.com"},
}


@app.post("/")
async def root(user: User):
    print(f"У юзера {user.name} такой id: {user.id}")
    return user


@app.get("/users")
async def read_users(limit: int = 10):
    return dict(list(fake_users.items())[:limit])


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}


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



def save_json(file: str, to_json: dict) -> None:
    with open(file, "w", encoding="utf-8") as f:
        json.dump(to_json, f, indent=4, ensure_ascii=False, separators=(',', ': '))


def load_json(file_name: str) -> dict:
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"user_msg": []}


Path('data.json').touch()
data = load_json("data.json")
# print(data)


@app.post("/feedback")
async def user_feedback(msg: Feedback):
    data["user_msg"].append({"name": msg.name, "message": msg.message})
    save_json("data.json", data)
    return {"message": f"Feedback received. Thank you, {msg.name}!"}




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
