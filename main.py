from typing import Annotated

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from repairs import schemas
from repairs.database import RepairRequestRepo

app = FastAPI()

db = RepairRequestRepo()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
  return templates.TemplateResponse(
    "index.html",
    {
      "request": request,
      "objects": db.all(),
    }
  )


@app.get("/get_by_id/{id}/", response_class=HTMLResponse)
def index(request: Request, id: int):
  return templates.TemplateResponse(
    "index.html",
    {
      "request": request,
      "objects": db.get(id),
    }
  )


@app.post("/create-repair-request/", response_class=HTMLResponse)
def create_repair_request(
  request: Request,
  data: Annotated[schemas.RepairRequestCreate, Form()],
  ):
  db.add(data)
  return templates.TemplateResponse(
    "index.html",
    {
      "request": request,
      "objects": db.all(),
      "message": "Repair request created",
    }
  )


@app.post("/update-repair-request/{id}/", response_class=HTMLResponse,)
def update_repair_request(
  request: Request,
  id: int,
  data: Annotated[schemas.RepairRequestCreate, Form()],
  ):
  db.update(id, data)
  return templates.TemplateResponse(
    "index.html",
    {
      "request": request,
      "objects": db.all(),
      "message": "Repair request updated",
    }
  )


@app.post("/delete-repair-request/{id}/", response_class=HTMLResponse)
def delete_repair_request(
  request: Request,
  id: int,
  ):
  db.remove(id)
  return templates.TemplateResponse(
    "index.html",
    {
      "request": request,
      "objects": db.all(),
      "message": "Repair request deleted",
    }
  )