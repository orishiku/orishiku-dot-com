from typing import Any, Callable, Set
from enum import Enum
from pydantic import (
    AliasChoices,
    AmqpDsn,
    BaseModel,
    Field,
    ImportString,
    PostgresDsn,
    RedisDsn,
)

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppName(str, Enum):
    main = "main"
    auth = "auth"


class AppSettings(BaseSettings):
    name: AppName
    port: int = 5000
    debug: bool = False

    model_config = SettingsConfigDict(env_prefix='app_')