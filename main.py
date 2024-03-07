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

@app.get("/users")
async def list_users():
    return {"message": "list users route"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

