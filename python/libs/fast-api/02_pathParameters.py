from fastapi import FastAPI

app = FastAPI()

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}#, read_item2(item_id)

# def read_item2(item_id: int):
#     return {"item_id2": item_id}


import uvicorn
if __name__ == "__main__":
    uvicorn.run("02_pathParameters:app", port=8000, host="127.0.0.1", reload=True)
