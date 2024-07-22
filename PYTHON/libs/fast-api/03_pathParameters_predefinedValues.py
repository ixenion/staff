# PREDEFINED VALUES

# If you have a path operation that receives a path parameter,
# but you want the possible valid path parameter values to be predefined,
# you can use a standard Python Enum.

from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# Path convertor
# Let's say you have a path operation with a path /files/{file_path}.
# But you need file_path itself to contain a path, like home/johndoe/myfile.txt.
# So, the URL for that file would be something like: /files/home/johndoe/myfile.txt
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

import uvicorn
from os import path as os_path
if __name__ == "__main__":
    script_name = os_path.basename(__file__).split('.')[0]
    uvicorn.run(f"{script_name}:app", port=8000, host="127.0.0.1", reload=True)
