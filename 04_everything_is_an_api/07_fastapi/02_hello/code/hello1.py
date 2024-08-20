from fastapi import FastAPI

app:FastAPI = FastAPI()

@app.get("/")
def index() -> str:
    return "Pakistanggg zinda bad , 123 , abc"

@app.get("/hi")
def greet():
    return "Hello World!"

@app.get("/hi/{name}")
def greet_with_name(name:str):
    return "Hello World!" + name

if __name__ in "__main__":
    import uvicorn 
    uvicorn.run("hello1:app", reload=True)