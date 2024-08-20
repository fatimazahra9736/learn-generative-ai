from fastapi import FastAPI , Body

app:FastAPI = FastAPI()

to_do = []

@app.post("/todo")
def greet(name:str = Body(),email:str = Body()):
    
    to_do.append({"name":name ,"email":email})
    return name

@app.get("/todo")
def todo():
    return to_do