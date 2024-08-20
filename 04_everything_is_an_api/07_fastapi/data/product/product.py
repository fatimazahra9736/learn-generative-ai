from fastapi import FastAPI,Header,Body, HTTPException
from pydantic import BaseModel

app:FastAPI = FastAPI()

class Products(BaseModel):
    product_name:str
    image_url:str
    prise:int
    quantity:int

list_products:list[Products] = []

@app.post("/")
def get_product(token:str = Header(),items:Products = Body()):
    if len(token) < 5 or len(token) > 10:
        raise HTTPException(status_code = 333, detail = "invalid token")
    list_products.append(items)
    return items

@app.get("/")
def produts_data():
    return list_products