from pydantic import BaseSettings, Field
from pydantic_settings import PydanticSettings
from pydantic_settings.settings import DatabaseSettings
from pydantic_settings.database import DatabaseDsn


class Databases(DatabaseSettings):
    DEFAULT: DatabaseDsn = Field(env="DATABASE_URL")
    SECONDARY: DatabaseDsn = Field(env="SECONDARY_DATABASE_URL")


class TestSettings(PydanticSettings):
    DATABASES: Databases = Field({})
