from fastapi import FastAPI, Header , Body, HTTPException 
from pydantic import BaseModel

app:FastAPI = FastAPI()

class Notifications(BaseModel):
    sender_name:str
    date:int
    description:str

list_notification:list[Notifications] = []

@app.post("/")
def get_notification(token:str = Header(), detail:Notifications = Body()):
    if len(token) < 5 or len(token) > 10:
        raise HTTPException(status_code = 333 , detail = "invalid token")
    list_notification.append(detail)
    return detail

@app.get("/")
def notification():
    return list_notification