from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

from models.models import User

app = FastAPI()


first_user = User(name="John Doe", id=1)


@app.post("/")
async def root(user: User):
    print(f"У юзера {user.name} такой id: {user.id}")
    return user


@app.get("/users", response_model=User)
async def users():
    return first_user


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
