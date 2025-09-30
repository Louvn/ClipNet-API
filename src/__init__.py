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

# Redirect to Docs
@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/redoc")

# Create db
from .database import Base, engine
from . import models

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# Routes
from .routes.auth import router as auth_router
from .routes.subwikis import router as subwikis_router

app.include_router(auth_router)
app.include_router(subwikis_router)