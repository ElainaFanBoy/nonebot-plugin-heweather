from typing import Optional

from nonebot import get_plugin_config
from pydantic import BaseModel, Field

from .model import HourlyType


class Config(BaseModel):
    qweather_apikey: Optional[str] = Field(default=None)
    qweather_apitype: Optional[str] = Field(default=None)
    qweather_hourlytype: Optional[HourlyType] = Field(default=HourlyType.current_12h)
    debug: bool = Field(default=False)


plugin_config: Config = get_plugin_config(Config)
QWEATHER_APIKEY = plugin_config.qweather_apikey
QWEATHER_APITYPE = plugin_config.qweather_apitype
QWEATHER_HOURLYTYPE = plugin_config.qweather_hourlytype
DEBUG = plugin_config.debug
