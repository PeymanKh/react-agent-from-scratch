"""
Configuration Management Module

Handles secure loading and validation of environment variables with support
for local .env files and cloud deployment with GCP Secret Manager integration.

Usage:
    from config.config import config

    if config.is_production():
        # Production-specific logic
        pass
"""
# Import libraries
import sys
import logging
from enum import Enum
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import SecretStr, Field, ValidationError


class LogLevel(str, Enum):
    """Standard logging levels for application logging configuration."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class SystemConfig(BaseSettings):
    """
    Main application configuration with environment-based loading.

    Supports local development with .env files and cloud deployment
    with environment variables from GCP Secret Manager.

    Read .env.example for more information about Environment Variables
    """

    # Application Settings with defaults
    app_name: str = Field(
        default="llm-engineering-12-week",
        description="Application identifier"
    )
    app_description: str = Field(
        default="LLM Engineering 12 Week Challenge",
        description="Application description"
    )
    app_version: str = Field(
        default="1.0.0",
        description="Application version"
    )
    app_author: str = Field(
        default="Peyman Khodabandehlouei",
        description="Application author"
    )
    environment: str = Field(
        default="development",
        description="Deployment environment"
    )
    debug: bool = Field(
        default=True,
        description="Enable debug mode"
    )

    # Logging Configuration with defaults
    log_level: LogLevel = Field(
        default=LogLevel.DEBUG,
        description="Logging level"
    )
    log_format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="Log message format string"
    )

    # LLM provider settings
    openai_api_key: SecretStr = Field(
        ...,
        description="OpenAI API key"
    )

    def is_production(self) -> bool:
        """Check if running in a production environment."""
        return self.environment.lower() == "production"

    def is_development(self) -> bool:
        """Check if running in a development environment."""
        return self.environment.lower() == "development"

    class Config:
        """Pydantic configuration for environment variable loading."""
        env_file = Path(__file__).parent.parent.parent / '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = False
        env_nested_delimiter = '__'


# Initialize logging with basic configuration
DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=DEFAULT_LOG_FORMAT)

# Load and validate configuration on module import
try:
    config = SystemConfig()
    logging.info(f"Configuration loaded for {config.environment} environment")
except ValidationError as e:
    logging.error(f"Configuration validation failed: {e}")
    sys.exit(1)
except Exception as e:
    logging.error(f"Failed to load configuration: {e}")
    sys.exit(1)


# Public API
__all__ = ['config', 'SystemConfig']
