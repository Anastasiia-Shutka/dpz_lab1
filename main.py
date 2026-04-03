import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from container import Container
from models.models import Base
from dal.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
container = Container()
templates = Jinja2Templates(directory="templates")

# --- READ (Список) ---
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    srv = container.exam_service()
    patients = srv.get_all_patients()
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"patients": patients}
    )

@app.get("/add", response_class=HTMLResponse)
async def add_form(request: Request):
    return templates.TemplateResponse(request=request, name="add.html")

@app.post("/add")
async def add_patient(
    full_name: str = Form(...), 
    dob: str = Form(...), 
    gender: str = Form(...), 
    history: str = Form("Не вказано")
):
    srv = container.exam_service()
    srv.create_patient(full_name, dob, gender, history)
    return RedirectResponse(url="/", status_code=303)

@app.get("/edit/{patient_id}", response_class=HTMLResponse)
async def edit_form(request: Request, patient_id: int):
    srv = container.exam_service()
    patient = srv.get_patient_by_id(patient_id)
    return templates.TemplateResponse(
        request=request, 
        name="edit.html", 
        context={"patient": patient}
    )

@app.post("/edit/{patient_id}")
async def update_patient(
    patient_id: int, 
    full_name: str = Form(...), 
    dob: str = Form(...), 
    gender: str = Form(...), 
    history: str = Form(...)
):
    srv = container.exam_service()
    srv.update_patient(patient_id, full_name, dob, gender, history)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete/{patient_id}")
async def delete_patient(patient_id: int):
    srv = container.exam_service()
    srv.delete_patient(patient_id)
    return RedirectResponse(url="/", status_code=303)

@app.post("/import")
async def run_import():
    srv = container.exam_service()
    srv.process_csv("patients.csv")
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)