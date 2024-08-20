from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

blogs = {
    "1" : "Generative AI blog",
    "2" : "Machin learning blog",
    "3" : "Deep learning blog",
}

users = {
    "8" : "Ahmad",
    "9" : "Muhammad",
}
def get_blog_or_404(id:str):
    name = blogs.get(id)
    if not name:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog id {id} not found")
    return name

app = FastAPI(title="Learn Dependency Injection")

@app.get("/blog/{id}")
def get_blogs(blog_name:Annotated[str , Depends(get_blog_or_404)] ):
    return blog_name