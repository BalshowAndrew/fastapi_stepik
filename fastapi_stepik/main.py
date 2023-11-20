from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class User(BaseModel):
    username: str
    age: int
    message: str
    

@app.post("/")
async def root(user: User):
    print(f"Мы получили от юзера {user.username}, которому {user.age} такое сообщение: {user.message}")
    return user

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
