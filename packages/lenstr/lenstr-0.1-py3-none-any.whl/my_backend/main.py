from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Mount the Streamlit app directory as a static file
app.mount("/streamlit", StaticFiles(directory="my_frontend"), name="streamlit")

# Serve index.html using templates for other routes
templates = Jinja2Templates(directory="my_frontend")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

    
uvicorn.run(app, host="127.0.0.1", port=8000)
