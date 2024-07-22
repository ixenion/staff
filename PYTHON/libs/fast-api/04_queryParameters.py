# When you declare other function parameters that are not part of
# the path parameters, they are automatically interpreted as "query" parameters.

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# In this case, if you go to:
# http://127.0.0.1:8000/items/foo?short=1
# http://127.0.0.1:8000/items/foo?short=True
# http://127.0.0.1:8000/items/foo?short=true
# http://127.0.0.1:8000/items/foo?short=on
# http://127.0.0.1:8000/items/foo?short=yes
# or any other case variation (uppercase, first letter in uppercase, etc),
# your function will see the parameter short with a bool value of True.
# Otherwise as False.

# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

import uvicorn
from os import path as os_path
if __name__ == "__main__":
    script_name = os_path.basename(__file__).split('.')[0]
    print(script_name)
    uvicorn.run(f"{script_name}:app", port=8000, host="127.0.0.1", reload=True)
