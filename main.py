from fastapi import FastAPI

# Initialize the application instance
app = FastAPI()

# Define a root route
@app.get("/")
def read_root():
    return {"message": "APP STARTED JUST NOW !!!"}

# Define a route with path and query parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query_q": q}
