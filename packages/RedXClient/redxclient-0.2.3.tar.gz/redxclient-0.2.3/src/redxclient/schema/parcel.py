from datetime import datetime

from pydantic import BaseModel
from typing_extensions import List


class DeliveryStatus(BaseModel):
    message_en: str
    message_bn: str
    time: datetime

class ParcelItemDetailsInput(BaseModel):
    name: str
    category: str
    value: float


class ParcelDetailsBase(BaseModel):
    customer_name: str
    customer_phone: str
    customer_address: str
    delivery_area: str
    delivery_area_id: int
    merchant_invoice_id: str = ""
    instruction: str = ""
    parcel_weight: int

class ParcelCreateInput(ParcelDetailsBase):
    value: int
    is_closed_box: bool
    cash_collection_amount: str
    parcel_details_json: List[ParcelItemDetailsInput]

class ParcelCreateResponse(BaseModel):
    tracking_id: str

class PickupLocation(BaseModel):
    id: int
    name: str
    address: str
    area_name: str
    area_id: int

class Parcel(ParcelDetailsBase):
    tracking_id: str
    status: str
    pickup_location: PickupLocation
    cash_collection_amount: int
    created_at: datetime
