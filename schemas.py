from datetime import date

from pydantic import BaseModel


class patientSchema(BaseModel):
    name: str
    dob: date
    email_id: str


class DoctorSchema(BaseModel):
    names: str
    dob: date
    education: str
    email_id: str
    dept_id: int

class Deptschema(BaseModel):
    dept:str
    description:str
