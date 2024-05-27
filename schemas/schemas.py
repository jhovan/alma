from pydantic import BaseModel
from fastapi import UploadFile
from ..common.constants import LeadStatus


class Lead(BaseModel):
    id: int
    state: LeadStatus

    class Config:
        from_attributes = True


class ProspectBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    lead_id: int


class ProspectCreate(ProspectBase):
    resume_file: UploadFile


class Prospect(ProspectBase):
    id: int
    resume_url: str

    class Config:
        from_attributes = True
