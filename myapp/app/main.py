import os
from fastapi import FastAPI, Request
import logging
import json
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

SERVICE_NAME = "myapplication"
VERSION = "1.0.0"
GIT_COMMIT_SHA = os.getenv("GIT_COMMIT_SHA", "local")
SERVICE_PORT = os.getenv("SERVICE_PORT", "8080")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

logging.basicConfig(level=LOG_LEVEL, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/info")
async def info(request: Request):
    response = {
        "service_name": SERVICE_NAME,
        "version": VERSION,
        "git_commit_sha": GIT_COMMIT_SHA,
        "environment": {
            "service_port": SERVICE_PORT,
            "log_level": LOG_LEVEL
        }
    }
    logger.info(json.dumps({
        "method": request.method,
        "path": request.url.path,
        "response": response
    }))
    return response

@app.get("/ui", response_class=HTMLResponse)
async def get_ui(request: Request):
    data = await info(request)  # Await since info is async
    return templates.TemplateResponse("info.html", {
        "request": request,
        "data": data
    })
