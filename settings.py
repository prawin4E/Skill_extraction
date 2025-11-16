"""
Application settings and configuration management.
"""
from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """Application settings with environment variable support"""

    # Application settings
    app_name: str = "Skill Extraction API"
    app_version: str = "0.1.0"
    debug: bool = False

    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000

    # CORS settings
    cors_origins: list = ["*"]

    # Logging settings
    log_level: str = "INFO"

    # SpaCy model settings
    spacy_model: str = "en_core_web_lg"

    # API settings
    api_v1_prefix: str = "/api/v1"

    # Rate limiting (requests per minute)
    rate_limit_per_minute: int = 60

    # Maximum resume text length (characters)
    max_resume_length: int = 50000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Create global settings instance
settings = Settings()
