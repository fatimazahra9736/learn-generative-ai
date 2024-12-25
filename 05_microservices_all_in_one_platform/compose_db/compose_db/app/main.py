from fastapi import FastAPI , Depends
from app import settings
from sqlmodel import Session, SQLModel, create_engine , Field , select
from contextlib import asynccontextmanager
from typing import Annotated, Optional

# connection_strin = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg")
connection_strin = str("postgresql://fatima:my_password@PostgresCont:5432/mydatabase").replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_strin)
def create_db()->None:
  SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app:FastAPI):
  create_db()
  print("DATABASE CREATED")
  yield

app = FastAPI(lifespan=lifespan , title="Hello World API" , 
              version= "0.0.1" ,
              servers=[
                  {
                    "url" : "http://localhost:9000",
                    "description" : "Development server"
                  }
              ]
            )

def get_session():
   with Session(engine) as session:
      yield session



class Names(SQLModel , table=True):
  id:Optional[int] = Field(primary_key=True ,default=None)
  name:str

  


   
@app.get("/")
def hello():
    return {"hello" : "world"}

@app.post("/add")
async def read_root(db:Annotated[Session , Depends(get_session)] , name:Names):
    
    create_name:Names = Names.model_validate(name)
    db.add(create_name)
    db.commit()
    db.refresh(create_name)
    return create_name

