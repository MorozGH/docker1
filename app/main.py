from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "I'm alive!"}

@app.get("/return/{item_id}")
async def return_item(item_id: int, description: str = None):
    return {"item_id": item_id, "description": description}