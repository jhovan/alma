from sqlalchemy.orm import Session

from ..models import models
from ..schemas import schemas
from ..common.constants import LeadStatus


def get_leads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lead).offset(skip).limit(limit).all()


def create_lead(db: Session):
    db_lead = models.Lead(state=LeadStatus.PENDING)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead


def update_lead(db: Session, lead_id: int, lead_state: LeadStatus):
    query = db.query(models.Lead).filter(models.Lead.id == lead_id)
    db_lead = query.one
    query.update({models.Lead.state: lead_state})
    db.commit()
    # db.refresh(db_lead)
    return db_lead
