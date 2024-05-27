from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..common.constants import LeadStatus
from .database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)
    state = Column(Enum(LeadStatus))

    prospect = relationship("Prospect", back_populates="lead")


class Prospect(Base):
    __tablename__ = "prospects"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    resume_url = Column(String)
    lead_id = Column(Integer, ForeignKey("leads.id"), unique=True)

    lead = relationship("Lead", back_populates="prospect")
