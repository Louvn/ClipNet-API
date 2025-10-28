# -- Env --
from dotenv import load_dotenv
load_dotenv()

# -- API --
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="ClipNet API",
    description="ClipNet is a modern Wiki System built with FastAPI",
    version="1.0.0"
)

# -- Serve React App --
import os
from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

react_build_path = os.path.join(os.path.dirname(__file__), "react-build")
app.mount("/static", StaticFiles(directory=os.path.join(react_build_path, "static")), name="static")

@app.get("/{full_path:path}", include_in_schema=False)
def serve_react_build(full_path):
    index_file = os.path.join(react_build_path, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return HTTPException(status_code=404, detail="index.html was not found")

# -- Create db -- 
from .database import Base, engine
from . import models

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# -- Routes for API --
from fastapi import APIRouter
from .routes.auth import router as auth_router
from .routes.articles import router as articles_router

api = APIRouter(prefix="/api")

api.include_router(auth_router)
api.include_router(articles_router)

app.include_router(api)