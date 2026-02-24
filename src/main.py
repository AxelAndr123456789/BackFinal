from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from src.apis.auth import router as auth_router
from src.apis.specialties import router as specialties_router
from src.apis.doctors import router as doctors_router
from src.apis.availability import router as availability_router
from src.apis.appointments import router as appointments_router
from src.apis.campaigns import router as campaigns_router
from src.apis.hospital import router as hospital_router

app = FastAPI(
    title="HealthConnect API",
    description="API para la aplicación móvil de citas médicas",
    version="1.0.0",
)


@app.middleware("http")
async def cors_middleware(request, call_next):
    origin = request.headers.get("origin")

    # Handle preflight
    if request.method == "OPTIONS":
        response = Response(status_code=200)
    else:
        response = await call_next(request)

    if origin:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Credentials"] = "true"
        response.headers["Access-Control-Allow-Methods"] = (
            "GET, POST, PUT, DELETE, OPTIONS, PATCH"
        )
        response.headers["Access-Control-Allow-Headers"] = (
            "Content-Type, Authorization, X-User-ID, Accept"
        )

    return response


app.include_router(auth_router, prefix="/api")
app.include_router(specialties_router, prefix="/api")
app.include_router(doctors_router, prefix="/api")
app.include_router(availability_router, prefix="/api")
app.include_router(appointments_router, prefix="/api")
app.include_router(campaigns_router, prefix="/api")
app.include_router(hospital_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "HealthConnect API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
