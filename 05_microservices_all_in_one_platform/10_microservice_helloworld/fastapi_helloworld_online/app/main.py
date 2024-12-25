from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"hello" : "world"}

@app.get("/piaic")
def piaic():
    return {"orgnaization" : "piaic"}
    