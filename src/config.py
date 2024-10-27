from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
        
    )
    # class Config:
    #     env_file = ".env"
        
print(Settings())
        
    