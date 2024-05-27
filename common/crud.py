from sqlalchemy.orm import Session

from ..models import models
from ..schemas import schemas


def get_leads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lead).offset(skip).limit(limit).all()
