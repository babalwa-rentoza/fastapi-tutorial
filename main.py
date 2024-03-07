from fastapi import FastAPI

# instantiate the app
app = FastAPI()

# setup a routes

@app.get("/")
async def base_get_route():
    return {"message": "hello world"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.put("/")
async def put():
    return {"message": "hello from the put route"}