from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .models import models
from .models.database import SessionLocal, engine
from .schemas import schemas
from .common import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/leads/", response_model=list[schemas.Lead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leads = crud.get_leads(db, skip=skip, limit=limit)
    return leads
