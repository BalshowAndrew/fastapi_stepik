from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/index", response_class=FileResponse)
async def root_index():
    return FileResponse("fastapi_stepik/index.html")


@app.post("/calculate")
async def root_calculate(num1: int, num2: int):
    return {"result": f"{num1 + num2}"}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
