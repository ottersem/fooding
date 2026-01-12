from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    # 옵션 1: 외부 호스팅에서 제공하는 MYSQL_URL 직접 사용
    mysql_url: Optional[str] = Field(default=None, alias="MYSQL_URL")
    
    # 옵션 2: 개별 변수 (MYSQL_URL이 없을 때 사용)
    db_username: str = Field(default="root", alias="MYSQLUSER")
    db_password: str = Field(default="password", alias="MYSQLPASSWORD")
    db_host: str = Field(default="localhost", alias="MYSQLHOST")
    db_port: int = Field(default=3306, alias="MYSQLPORT")
    db_name: str = Field(default="fooding", alias="MYSQLDATABASE")

    model_config = SettingsConfigDict(
        env_file=".env",
        populate_by_name=True,  # 필드명과 alias 모두 인식
    )

    @property
    def db_url(self) -> str:
        # MYSQL_URL이 제공된 경우 그것을 사용
        if self.mysql_url:
            return self.mysql_url
        
        # 그렇지 않으면 개별 변수로 구성
        return (
            f"mysql+pymysql://{self.db_username}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


settings = Settings()
