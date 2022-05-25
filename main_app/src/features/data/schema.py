from enum import Enum
from typing import Union

from pydantic import BaseModel


#
class CountriesEnum(str, Enum):
    POLAND = 'PL'


class KeysEnum(str, Enum):
    AMENITY = 'amenity'


class AmenityEnum(str, Enum):
    ZIP_LINE = 'zip_line'
    RESTAURANT = 'restaurant'


class OSMQuery(BaseModel):
    country: str
    admin_level: int
    key: KeysEnum
    value: Union[AmenityEnum]
