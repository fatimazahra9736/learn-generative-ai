from sqlmodel import create_engine , Session , SQLModel , select , Field 
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends , Body ,HTTPException, status , Response
from typing import Annotated 
from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta
from myproject.service import hashed_pass , verify_pass , create_token , verify_token
from myproject.service import ACCESS_TOKEN_EXPIRE_MINUTES
from myproject.model.model import ToDo,TodoBase,TodoCreate,TodoResponse,TodoUpdate,Token,TokenData,Users,UsersCreate,UsersLogin

db_url = "postgresql+psycopg://neondb_owner:W4aRIH5mgxKU@ep-autumn-term-a5o4pwas.us-east-2.aws.neon.tech/neondb?options=endpoint%3Dep-autumn-term-a5o4pwas"
conn_str =str(db_url)
engine = create_engine(conn_str , connect_args={"sslmode": "require"}, pool_recycle=300)

origins = [
    
    "http://localhost:3000",
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is running")
    create_db()
    yield

def create_db():
    SQLModel.metadata.create_all(engine)
    print("database created")
def get_session():
    with Session(engine) as sess:
        yield sess

app:FastAPI = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/signup" , response_model=Token)
async def sign_up(db:Annotated[Session , Depends(get_session)] , users:UsersCreate):
    check_user:Users = select(Users).where(Users.email == users.email)
    result = db.exec(check_user).first()
    if result != None:
        raise HTTPException(status_code= 404 , detail="User already added")
    else :
        users.password = hashed_pass(users.password)
        create_user:Users = Users.model_validate(users)
        db.add(create_user)
        db.commit()
        token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_token(data={"email" : create_user.email} , expire_delta= token_expire)
        return Token(access_token=token , token_type="bearer")
    
@app.post("/login" )
async def log_in(db:Annotated[Session , Depends(get_session)] , login_user:UsersLogin , response:Response):
    check_email = select(Users).where(Users.email == login_user.email)
    result:Users = db.exec(check_email).first()
    if result is not None:
        if not verify_pass(login_user.password , result.password):
            raise HTTPException(status_code=201 , detail = "invalid email or password")
        else: 
            token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            token = create_token(data={"email" : result.email , "id" : result.id} , expire_delta= token_expire)
            token_type = "bearer"
            response.headers["authorization"] = token
            response.headers["type"] = token_type
            # return Token(access_token=token , token_type=token_type)
            return {
                "massage":"user successfully login"
            }
    else:
        raise HTTPException(status_code=201 , detail = "user not found")

@app.get("/user" , response_model=Users)
async def get_user(db:Annotated[Session , Depends(get_session)] , token_data:Annotated[TokenData , Depends(verify_token)]):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Could not validate credentials" , headers={"WWW-Authenticat":"Bearer"})
    if token_data.email is None:
        raise exception
    else:
        statment = select(Users).where(Users.email == token_data.email)
        result = db.exec(statment).one()
        if not result:
            raise exception
        return result


@app.post("/add" , response_model=TodoResponse)
async def create_todo(db:Annotated[Session , Depends(get_session)] , todo:TodoCreate , token_data:Annotated[TokenData , Depends(verify_token)]):
    db_user = db.get(Users , token_data.id)
    if not db_user:
       raise HTTPException(status_code=404 , detail = "user not found")
    todoObj:ToDo = ToDo.model_validate(todo)
    todoObj.users = db_user
    todoObj.user_id = db_user.id
    db.add(todoObj)
    db.commit()
    db.refresh(todoObj)
    return todoObj

@app.get("/gettodos" , response_model=list[TodoResponse])
async def get_todo(db:Annotated[Session , Depends(get_session)] , token_data:Annotated[TokenData , Depends(verify_token)]):
    user_todo:ToDo = select(ToDo).where(ToDo.user_id == token_data.id)
    try:
        result = db.exec(user_todo).all()
        return result
    except:
        raise HTTPException(status_code=505 , detail = "Todo not found")
     
@app.get("/mytodo/{id}" , response_model=TodoResponse)
async def my_todo(db:Annotated[Session , Depends(get_session)] , token_data:Annotated[TokenData , Depends(verify_token)] , id:int):
    mytodo:ToDo = select(ToDo).where(ToDo.user_id == token_data.id).where(ToDo.id == id)
    my_result = db.exec(mytodo).first()
    if my_result != None:
        return my_result
    else:
        raise HTTPException(status_code=505 , detail = "ID not found")

@app.patch("/update" , response_model=TodoResponse , dependencies=[Depends(verify_token)])
async def update_todo(db:Annotated[Session , Depends(get_session)], todo_id:int ,todo:TodoUpdate):
    db_todo = db.get(ToDo ,todo_id)  
    if not db_todo:
        raise HTTPException(status_code=404, detail="User not found")
    todo_data = todo.model_dump(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(db_todo, key, value)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/delete/{id}" , dependencies=[Depends(verify_token)])
async def delete_todos(id:int , db:Annotated[Session , Depends(get_session)]):
    try:
        item = db.get(ToDo , id)
        db.delete(item)
        db.commit()
        return {
        "message":"todo deleted "
        }
    except:
        raise HTTPException(status_code=505 , detail = "User not found")