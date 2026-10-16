from fastapi import APIRouter
from routers.posts import patients, doctors,dept

from fastapi import HTTPException
router=APIRouter()  

@router.get("/getpatient/{id}")

def get_patient(id:int):
    for patient in patients:
        if patient["id"]==id:
            return patient
    raise HTTPException(status_code=404,detail="Patient not found")

@router.get("/allpatients")
def get_allpatient():
    return patients

@router.get("/getdoctor/{id}")

def getdoctor(id:int):
    for doctor in doctors:
        if doctor["id"]==id:
            return doctor
    raise HTTPException(status_code=404,detail="Doctor Not Found")


@router.get("/alldoctors")
def get_alldoctor():
    return doctors


@router.get("/getdepartment/{id}")

def getdept(id:int):
    for dpt in dept:
        if dpt["id"]==id:
            return dpt
    raise HTTPException(status_code=404,detail="Department not found")

@router.get("/alldep")

def alldept():
    return dept


