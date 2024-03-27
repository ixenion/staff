from fastapi import FastAPI

app = FastAPI()


# get - http method (post, put, delay)
@app.get("/")
async def root():
    return {"message": "Hello World"}

# launch server
# uvicorn main:app --reload

# main - module that we use
# app - app instance
# --reload - automatically reload the app after code changed

# now open
# http://127.0.0.1:8000

# see docs generated automatically
# http://127.0.0.1:8000/docs

# run uviocrn from script
import uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
