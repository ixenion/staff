from fastapi import FastAPI
import uvicorn

from db.base import database

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# move here from db/base.py (1)
@app.on_event
async def startup():
    # connect to the database
    await database.connect()

# handler app shutdown 
# it's nessesary to free "request pull"
# to the db
@app.on_event("shutdown")
async def shutdown():
    # disconnect from db
    await database.disconnect()
# now app is able to connect to the db

# to connect to the db
# first - need to startup it
# 1. create env vars
# export EE_DATABASE_URL="postgresql://root:root@localhost:32700/employ_exchange"
# 2. create docker-compose.dev.yaml
# 3. start docker-compose
# docker compose -f docker-compose.dev.yaml up

# to stop dockerd servise
# sudo systemctl stop docker



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
