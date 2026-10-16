from fastapi.testclient import TestClient
from main import app
from routers.posts import patients, doctors, dept

client = TestClient(app)


def test_create_and_read_patient():
    patients.clear()
    r = client.post("/api/newpatient", json={
        "name": "Anu", "dob": "2003-09-07", "email_id": "anu@test.com"})
    assert r.status_code == 200
    r2 = client.get("/api/getpatient/1")
    assert r2.status_code == 200
    assert r2.json()["name"] == "Anu"


def test_patient_not_found():
    patients.clear()
    r = client.get("/api/getpatient/99")
    assert r.status_code == 404
    assert r.json()["detail"] == "Patient not found"


def test_bad_date_is_rejected():
    patients.clear()
    r = client.post("/api/newpatient", json={
        "name": "Anu", "dob": "not-a-date", "email_id": "anu@test.com"})
    assert r.status_code == 422
    assert len(patients) == 0


def test_create_and_read_department():
    dept.clear()
    r = client.post("/api/newdept", json={
        "dept": "Cardiology", "description": "Heart"})
    assert r.status_code == 200
    r2 = client.get("/api/getdepartment/1")
    assert r2.json()["department"] == "Cardiology"


def test_department_not_found():
    dept.clear()
    r = client.get("/api/getdepartment/99")
    assert r.status_code == 404


def test_create_and_read_doctor():
    doctors.clear()
    r = client.post("/api/newdoctor", json={
        "names": "Dr. Thomas", "dob": "1985-04-07", "education": "MBBS",
        "email_id": "t@hospital.com", "dept_id": 1})
    assert r.status_code == 200
    r2 = client.get("/api/getdoctor/1")
    assert r2.json()["name"] == "Dr. Thomas"


def test_doctor_not_found():
    doctors.clear()
    r = client.get("/api/getdoctor/99")
    assert r.status_code == 404