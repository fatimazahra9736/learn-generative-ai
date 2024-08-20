from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated, Any

blogs = {
    "1" : "generative AI blog",
    "2" : "machine learning blog",
    "3" : "deep learning blog",
}

users  = {
    "8" : "Ahmad",
    "9" : "Muhammad",
}

class GetObjectOr404():
    def __init__(self , model) -> None:
        self.modle = model

    def __call__(self, id:str) -> Any:
        obj = self.modle.get(id)
        if not obj:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"object ID {id} not found")
        return obj
app = FastAPI(title="Learn Dependency Injection")

blog_dependencies = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blogs(blog_name:Annotated[str , Depends(blog_dependencies)]):
    return blog_name

user_dependencies = GetObjectOr404(users)

@app.get("/user/{id}")
def get_users(user_name:Annotated[str , Depends(user_dependencies)]):
    return user_name