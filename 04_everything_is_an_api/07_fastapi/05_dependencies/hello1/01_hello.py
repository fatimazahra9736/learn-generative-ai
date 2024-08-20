from fastapi import FastAPI , Query , Depends
from typing import Annotated

app:FastAPI = FastAPI()

def dep_login(username:str = Query(None) , password:str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message" : "Log in successful"}
    
    else:
        return {"message" : "Log in failed"}
    
@app.get("/signin")
def login_api(user:Annotated[dict,Depends(dep_login)]):
    return user
