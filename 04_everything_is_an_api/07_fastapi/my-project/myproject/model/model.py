from sqlmodel import Field , SQLModel, Relationship
from typing import List, Optional, Union

class UsersLogin(SQLModel):
    email:str
    password:str

class UsersCreate(UsersLogin):
    firstname:str
    lastname:str

class Users(UsersCreate , table = True):
    id:int = Field(default=None , primary_key=True)
    todo:list["ToDo"] = Relationship(back_populates="users")

class Token(SQLModel):
    access_token:str
    token_type:str

class TokenData(SQLModel):
    id:int | None = None
    email:str

class TodoBase(SQLModel):
    title:str
    description:str

class ToDo(TodoBase,table = True):
    id:int = Field(default=None , primary_key=True)
    status:bool = Field(default=False)
    users:Optional[Users] = Relationship(back_populates="todo")
    user_id:Optional[int] = Field(default=None , foreign_key="users.id")
    
class TodoCreate(TodoBase):
    pass
   
class TodoResponse(TodoBase):
    id:int
    status:bool

class TodoUpdate(TodoBase):
    title:str | None = None
    description:str | None = None