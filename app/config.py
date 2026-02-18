class Settings:
    SECRET_KEY = "your_super_secret_key_here" 
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    DEFAULT_ACCESS_DURATION_SECONDS = 3600 

settings = Settings()