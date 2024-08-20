from sqlmodel import create_engine , Session , SQLModel , select , Field
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends , Body
from typing import Annotated 

db_url = "postgresql+psycopg://neondb_owner:W4aRIH5mgxKU@ep-autumn-term-a5o4pwas.us-east-2.aws.neon.tech/neondb?options=endpoint%3Dep-autumn-term-a5o4pwas"
conn_str =str(db_url)
engine = create_engine(conn_str , connect_args={"sslmode": "require"}, pool_recycle=300)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is running")
    create_db()
    yield

class ToDo(SQLModel,table = True):
    id:int = Field(default=None , primary_key=True)
    name:str
    title:str

def create_db():
    SQLModel.metadata.create_all(engine)
    print("database created")
def get_session():
    with Session(engine) as sess:
        yield sess

app:FastAPI = FastAPI(lifespan=lifespan)

@app.post("/add")
def create_todo(db:Annotated[Session , Depends(get_session)] , user:ToDo = Body()):
    userObj:ToDo = ToDo(name= user.name , title= user.title)
    db.add(userObj)
    db.commit()
    db.close()
    return user

@app.get("/get")
def get_todo(db:Annotated[Session , Depends(get_session)]):
    user_todo:ToDo = select(ToDo)
    result = db.exec(user_todo).all()
    return result 

@app.get("/mytodo/{id}")
def my_todo(id:int , db:Annotated[Session , Depends(get_session)]):
    mytodo:ToDo = select(ToDo).where(ToDo.id == id)
    my_result = db.exec(mytodo).first()
    return my_result

@app.post("/update")
def update_todo(db:Annotated[Session , Depends(get_session)] , update_todo:ToDo = Body() , for_update:ToDo = Body()):
    gettodo = select(ToDo).where(ToDo.name == update_todo.name).where(ToDo.title == update_todo.title)
    updated_todo = db.exec(gettodo).one()
    updated_todo.name = for_update.name
    updated_todo.title = for_update.title
    db.add(updated_todo)
    db.commit()
    db.refresh(updated_todo)
    return updated_todo

@app.get("/delete/{name}")
def delete_todo(name:str , db:Annotated[Session , Depends(get_session)]):
    statement:ToDo = select(ToDo).where(ToDo.name == name)
    delete_todo = db.exec(statement).one()
    db.delete(delete_todo)
    db.commit()
    return delete_todo
