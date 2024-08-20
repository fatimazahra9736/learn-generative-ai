from fastapi import FastAPI , Query , Depends

app:FastAPI = FastAPI()

def dep_check(name:str = Query(None) , password:str = Query(None)):
    if not name:
        raise

@app.get("/login", dependencies = [Depends(dep_check)])
def log_in():
    return True