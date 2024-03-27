from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

import uvicorn
from os import path as os_path
if __name__ == "__main__":
    script_name = os_path.basename(__file__).split('.')[0]
    uvicorn.run(f"{script_name}:app", port=8000, host="127.0.0.1", reload=True)
