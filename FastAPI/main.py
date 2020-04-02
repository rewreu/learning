from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    # item.pred = 9
    print(item.json())
    print(type(item.json()))
    print(item.to_string())
    it = item.dict()
    it["pred"] = 9
    return it