import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    database_url: str = os.getenv("DATABASE_URL", "postgresql://localhost/wellnessconnect")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # WhatsApp
    whatsapp_access_token: str = os.getenv("WHATSAPP_ACCESS_TOKEN", "")
    whatsapp_phone_number_id: str = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
    whatsapp_webhook_verify_token: str = os.getenv("WHATSAPP_WEBHOOK_VERIFY_TOKEN", "")
    
    # AI
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    
    # Application
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    environment: str = os.getenv("ENVIRONMENT", "development")
    
    # External Services
    google_translate_api_key: Optional[str] = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    twilio_account_sid: Optional[str] = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token: Optional[str] = os.getenv("TWILIO_AUTH_TOKEN")
    
    # Scheduling
    calendar_api_key: Optional[str] = os.getenv("CALENDAR_API_KEY")
    
    class Config:
        env_file = ".env"

settings = Settings()