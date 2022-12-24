from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = "tester@example.com"
    items_per_user: int = 50

    class Config:
        env_file = ".env"