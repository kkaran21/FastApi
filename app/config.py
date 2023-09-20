#config.py
from pydantic import BaseSettings

class Settings (BaseSettings):
    server_name:str
    database_name:str
    secret_key:str
    algorithm:str
    token_expiration_time_minutes:int
    

    class Config:
        env_file= ".env"

settings=Settings()




