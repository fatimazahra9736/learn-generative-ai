from fastapi import FastAPI, Header , Body, HTTPException 
from pydantic import BaseModel

app:FastAPI = FastAPI()

class LogIn(BaseModel):
    firstname:str
    lastname:str
    email:str
    password:str

loginarr:list[LogIn] = []
@app.post("/")
def log_in(token:str = Header(),login:LogIn = Body()):
    if len(token) < 5 or len(token)>10:
      raise HTTPException(status_code = 333 , detail = "invalid token")
    loginarr.append(login)
    return token

@app.get("/")
def getheader():
    return loginarr

 