from fastapi import APIRouter
from schemas import patientSchema,DoctorSchema,Deptschema
router=APIRouter()
patients=[]
dept=[]
doctors=[]
# register new patient
@router.post("/newpatient")

def create_patient(patient:patientSchema):
        
    
    
        new_patient= {
        "id":len(patients)+1,
        "name":patient.name,
        "dob":patient.dob,
        "email_id":patient.email_id  }

        patients.append(new_patient)
        return {"message":f"{patient.name} ,{new_patient['id']} is created sucessfully"}
    
     
    
    
@router.post("/newdoctor")

def create_doctor(doctor:DoctorSchema):
        doc_new={
                "id":len(doctors)+1,
                "name":doctor.names,
                "dept_id":doctor.dept_id,
                "dob":doctor.dob,
                "emailid":doctor.email_id,
                "education":doctor.education
        }
        doctors.append(doc_new)
        return{"message":f"{doctor.names} is created and the empid is {doc_new['id']}"}

@router.post("/newdept")
def createdept(deptmnt:Deptschema):
        deptd={
                "id":len(dept)+1,
                "department":deptmnt.dept,
                "description":deptmnt.description
        }
        dept.append(deptd)
        return{"message":f"{deptmnt.dept} is created and the id is {deptd['id']}"}
