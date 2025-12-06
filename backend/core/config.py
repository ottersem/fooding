from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_host: str = "localhost"
    db_port: int = 3307
    db_name: str

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def db_url(self) -> str:
        return (
            f"mysql+pymysql://{self.db_username}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


settings = Settings()
