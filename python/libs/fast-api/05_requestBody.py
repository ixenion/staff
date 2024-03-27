from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
# test it!
# curl -X POST -H "Content-Type: application/json" -d '{"name": "apple", "price": 42.0}' http://localhost:8000/items/

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
# test it
# curl -X PUT -H "Content-Type: application/json" -d '{"name": "apple", "price": 42.0}' http://localhost:8000/items/3

import uvicorn
from os import path as os_path
if __name__ == "__main__":
    script_name = os_path.basename(__file__).split('.')[0]
    uvicorn.run(f"{script_name}:app", port=8000, host="127.0.0.1", reload=True)

