from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """
    Application configuration using Pydantic Settings.
    (Encapsulation) - Configuration values are managed in a single, type-safe class.
    """
    
    # Database Configuration
    db_host: str = Field(default="localhost", alias="DB_HOST")
    db_user: str = Field(default="root", alias="DB_USER")
    db_password: str = Field(default="", alias="DB_PASSWORD")
    db_name: str = Field(default="prototype_afturshop", alias="DB_NAME")
    
    # Application Settings
    app_name: str = Field(default="Aftur Shop API", alias="APP_NAME")
    app_version: str = Field(default="1.0.0", alias="APP_VERSION")
    debug: bool = Field(default=True, alias="DEBUG")
    
    # Upload Settings
    upload_dir: str = Field(default="uploads", alias="UPLOAD_DIR")
    max_upload_size: int = Field(default=5242880, alias="MAX_UPLOAD_SIZE")  # 5MB
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
    
    @property
    def database_url(self) -> str:
        """Generate SQLAlchemy database URL."""
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}"


# Global settings instance
settings = Settings()
