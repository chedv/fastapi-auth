from pydantic import BaseSettings


class Settings(BaseSettings):
    app_host: str
    app_port: int

    db_user: str
    db_pwd: str
    db_name: str
    db_host: str
    db_port: int
    db_echo: bool

    jwt_secret: str

    class Config:
        env_file = '.env'


settings = Settings()
