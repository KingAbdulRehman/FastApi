# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# @app.post("/items/")
# def create_item(name: str, price: float):
#     return {"name": name, "price": price}

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Set up templates directory
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Pass data to HTML template
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello from FastAPI!"})

@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}

# Run the app with Uvicorn (you can also run from terminal)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

