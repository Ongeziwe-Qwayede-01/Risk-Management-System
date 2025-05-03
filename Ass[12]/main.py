 
from fastapi import FastAPI
from api.risk_api import router as risk_router
from api.user_api import router as user_router
from api.mitigation_plan_api import router as plan_router

app = FastAPI(title="Risk Management System API")

# Register route modules
app.include_router(risk_router, prefix="/api")
app.include_router(user_router, prefix="/api")
app.include_router(plan_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the Risk Management System API"}
