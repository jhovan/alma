from pydantic import BaseModel
from fastapi import File
from common.constants import LeadStatus


class Lead(BaseModel):
    id: int
    state: LeadStatus

    class Config:
        orm_mode = True

class ProspectBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    lead_id: int

class ProspectCreate(ProspectBase):
    resume_file: File

class Prospect(ProspectBase):
    id: int
    resume_url: str

    class Config:
        orm_mode = True