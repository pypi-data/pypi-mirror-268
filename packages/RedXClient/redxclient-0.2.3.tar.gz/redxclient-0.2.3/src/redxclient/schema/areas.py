from enum import IntEnum

from pydantic import BaseModel, ValidationError, model_validator
from typing_extensions import Any, Optional, Self


class ZoneEnum(IntEnum):
    DHAKA_CITY = 1
    DHAKA_SUBURBS = 2
    OUTSIDE_DHAKA = 7


class Area(BaseModel):
    id: int
    name: str
    post_code: Optional[int] = None
    district_name: str
    division_name: str
    zone_id: ZoneEnum


class AreaFilter(BaseModel):
    zone_id: Optional[ZoneEnum] = None
    post_code: Optional[int] = None
    name: Optional[str] = None

    @model_validator(mode="after")
    def check_mutual_exclusivity(self) -> Self:
        flag = False
        for field in self.model_dump().values():
            if field is not None:
                if flag:
                    raise ValueError("Only one of zone_id, post_code, name is allowed")
                flag = True
        return self
