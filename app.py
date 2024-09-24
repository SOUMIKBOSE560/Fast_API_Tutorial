from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/')
def test():
    return "Hello server"

@app.post('/list')
def create_item(item: str):
    return {"message": f"Item {item} created"}

# raising error
@app.post('/testerror')
def test_error(item: str):
    raise HTTPException(status_code=400, detail="Item already exists")

@ app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# fastAPI swagger UI page add after main uri --> docs#/