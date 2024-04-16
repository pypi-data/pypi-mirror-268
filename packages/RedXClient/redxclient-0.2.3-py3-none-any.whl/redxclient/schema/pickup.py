from datetime import datetime

from pydantic import BaseModel


class PickupStoreBase(BaseModel):
    name: str
    address: str
    phone: str
    area_id: int

class PickupStoreInput(PickupStoreBase):
    pass

class PickupStoreCreateResponse(PickupStoreBase):
    id: int

class PickupStore(PickupStoreBase):
    id: int
    area_name: str
    created_at: datetime
