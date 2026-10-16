from fastapi import FastAPI
from routers.posts import router as patient_router
from routers.get import router as getrouter
app = FastAPI()
app.include_router(patient_router, prefix="/api")

app.include_router(getrouter,prefix="/api")
@app.get("/health")
def healthcheck():
    return {"status": "ok"}