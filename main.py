from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .models import models
from .models.database import SessionLocal, engine
from .schemas import schemas
from .common import crud
from .common.constants import LeadStatus

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/leads/create", response_model=schemas.Lead)
def create_lead(db: Session = Depends(get_db)):
    return crud.create_lead(db=db)


@app.get("/leads/", response_model=list[schemas.Lead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leads = crud.get_leads(db=db, skip=skip, limit=limit)
    return leads

@app.put("/leads/{lead_id}/update", response_model=schemas.Lead)
def update_lead(lead_id: int, state: LeadStatus = LeadStatus.REACHED_OUT, db: Session = Depends(get_db)):
    return crud.update_lead(db=db, lead_id=lead_id, lead_state=state)