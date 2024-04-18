from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict, BaseSettings
from typing import Any, Optional, Union, get_args
from transpara import tlogging
from transpara.tlogging import TRANSPARA_DEBUG_LEVEL
from os import getenv
import requests

#Setting verbose logging, once we get settings from tSystem we can set the actual value
tlogging.set_log_level(TRANSPARA_DEBUG_LEVEL)

logger = tlogging.get_logger(__name__)

class BaseRequiredSettings(BaseSettings):
    TSYSTEM_HOST: str = "tsystem_api"
    ALLOW_OFFLINE: bool = True
    IMAGE_TAG: str =  "0.0.0"
    VERSION: str = "0.0.6"
    COMPONENT_ID: str = "049f6ed7-e754-4315-bdc6-bf5ed6e4d437"
    TSYSTEM_COMPONENT_TYPE: str = "tgraphs"
    model_config = SettingsConfigDict(case_sensitive=True)

required_settings = BaseRequiredSettings()

class BaseTSystemSettings(BaseModel):    

    LOG_LEVEL: Optional[Union[str,int]] = TRANSPARA_DEBUG_LEVEL
    LOG_GLOBAL_VERBOSE: Optional[bool] = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_settings()


    def __env_to_bool(self, v: Any) -> bool:    
        if isinstance(v, bool):
            return v
        if isinstance(v, str):
            return v.lower() in ("yes", "true", "t", "1")
        return bool(v)

    def __env_to_int(self, v: Any) -> bool:    
        try:
            return int(v)
        except:
            return v
        
    def __env_to_float(self, v: Any) -> bool:
        try:
            return float(v)
        except:
            return v

    def load_settings(self):
        try:
            response = requests.get(f"http://{required_settings.TSYSTEM_HOST}/{required_settings.TSYSTEM_COMPONENT_TYPE}/{required_settings.COMPONENT_ID}")
            response.raise_for_status()
            settings: dict = response.json()["settings"]
            for key, value in settings.items():
                if hasattr(self, key): 
                    setattr(self, key, value)
        except:
        
            logger.terror(f"Failed to get settings from tSystem")

            if not required_settings.ALLOW_OFFLINE:
                logger.terror("Can't get settings from tSystem, and it is not allowed to run offline")
                raise
        
            logger.tdebug("Running offline, using settings from env")
            self.load_from_env()

    def load_from_env(self):
        for key, field in self.model_fields.items():
            try:
                value = getenv(key)
                
                types = get_args(field.annotation) or [field.annotation]

                if value is None:
                    continue
                
                if bool in types:
                    setattr(self, key, self.__env_to_bool(value))
                elif int in types:
                    setattr(self, key, self.__env_to_int(value))
                elif float in types:
                    setattr(self, key, self.__env_to_float(value))
                else:
                    setattr(self, key, value)
            except:
                logger.warning(f"Failed to load {key} from env and tSystem, falling back to {field.default}")

base_tsystem_settings = BaseTSystemSettings()

tlogging.set_log_level(base_tsystem_settings.LOG_LEVEL)
tlogging.set_global_verbose(base_tsystem_settings.LOG_GLOBAL_VERBOSE)