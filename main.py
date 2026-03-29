import uvicorn
from fastapi import FastAPI
from container import Container
from models.models import Base, Patient
from dal.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
container = Container()

@app.post("/import-data")
def import_csv():
    srv = container.exam_service()
    srv.process_csv("patients.csv")
    return {"status": "ok"}

@app.get("/check-db")
def check():
    session_factory = container.db_session()
    with session_factory() as session: 
        count = session.query(Patient).count()
        return {"total_records_in_db": count}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)