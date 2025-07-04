from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import webhook, appointments, leads, analytics, whitelabel
from src.api.middleware.auth import AuthMiddleware
from src.api.middleware.rate_limiting import RateLimitMiddleware
from config.settings import settings
from config.database import init_db

app = FastAPI(
    title="WellnessConnect",
    description="AI-Powered Health Concierge Platform",
    version="1.0.0"
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(AuthMiddleware)
app.add_middleware(RateLimitMiddleware)

# Routes
app.include_router(webhook.router, prefix="/api")
app.include_router(appointments.router, prefix="/api")
app.include_router(leads.router, prefix="/api")
app.include_router(analytics.router, prefix="/api")
app.include_router(whitelabel.router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
async def root():
    return {"message": "WellnessConnect API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)