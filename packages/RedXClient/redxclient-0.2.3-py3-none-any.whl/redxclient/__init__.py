import requests
from typing_extensions import Any, List, Literal, Optional

from redxclient.schema.areas import Area, AreaFilter
from redxclient.schema.pickup import (
    PickupStore,
    PickupStoreCreateResponse,
    PickupStoreInput,
)

from .schema.parcel import DeliveryStatus, Parcel, ParcelCreateInput

BETA_API_URL = "https://sandbox.redx.com.bd/v1.0.0-beta"
PRODUCTION_API_URL = "https://openapi.redx.com.bd/v1.0.0-beta"


class RedXAPIClient:
    """RedX API Client"""

    def __init__(self, api_key: str, base_url=BETA_API_URL) -> None:
        """Initialize the RedX API Client

        Args:
            api_key (str): API Key
            base_url (str, optional): Base URL of the API. Defaults to BETA_API_URL.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _get_headers(self) -> dict[str, str]:
        return {
            "API-ACCESS-TOKEN": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _perform_request(
        self,
        method: Literal["GET"] | Literal["POST"],
        path: str,
        data: Optional[dict[str, Any] | bytes] = None,
    ) -> Any:
        headers = self._get_headers()
        response = requests.request(
            method,
            f"{self.base_url}/{path}",
            headers=headers,
            data=data if method == "POST" else None,
            params=data if method == "GET" else None,
        )
        response.raise_for_status()
        return response.json()

    def track_percel(self, tracking_id: str) -> List[DeliveryStatus]:
        """Track a parcel by tracking id

        Args:
            tracking_id (str): Tracking ID of the parcel

        Returns:
            List[DeliveryStatus]: List of delivery status
        """
        url = f"{self.base_url}/parcel/track/{tracking_id}"
        response = self._perform_request("GET", f"parcel/track/{tracking_id}")
        return [DeliveryStatus(**status) for status in response["tracking"]]

    def create_parcel(self, data: dict[str, Any] | ParcelCreateInput) -> str:
        """Create a parcel

        Args:
            data (dict[str, Any] | ParcelCreateInput): Parcel data

        Returns:
            str: Tracking ID of the created parcel
        """
        valid = ParcelCreateInput(**data) if isinstance(data, dict) else data
        response = self._perform_request(
            "POST", "parcel", valid.model_dump_json(round_trip=True).encode("utf-8")
        )
        return response["tracking_id"]

    def get_parcel_details(self, tracking_id: str) -> Parcel:
        """Get parcel details by tracking id

        Args:
            tracking_id (str): Tracking ID of the parcel

        Returns:
            Parcel: Parcel details
        """
        response = self._perform_request("GET", f"parcel/info/{tracking_id}")
        return Parcel(**response["parcel"])

    def get_areas(
        self, filters: Optional[AreaFilter | dict[str, Any]] = None
    ) -> List[Area]:
        """Get areas

        Args:
            filters (AreaFilter | dict[str, Any], optional): Filters for the areas. Defaults to None.

        Returns:
            List[Area]: List of areas
        """
        params = {}
        if filters:
            validator: AreaFilter = (
                AreaFilter(**filters) if isinstance(filters, dict) else filters
            )
            params = validator.model_dump()
        response = self._perform_request("GET", "areas", params)
        return [Area(**area) for area in response["areas"]]

    def create_pickup_store(
        self, data: PickupStoreInput | dict
    ) -> PickupStoreCreateResponse:
        """Create a pickup store

        Args:
            data (PickupStoreInput | dict): Pickup store data

        Returns:
            PickupStoreCreateResponse: Response of the created pickup store
        """
        valid = PickupStoreInput(**data) if isinstance(data, dict) else data
        response = self._perform_request(
            "POST", "pickup/store", valid.model_dump_json().encode("utf-8")
        )
        return PickupStoreCreateResponse(**response)

    def get_pickup_stores(self) -> List[PickupStore]:
        """Get pickup stores

        Returns:
            List[PickupStore]: List of pickup stores
        """
        response = self._perform_request("GET", "pickup/stores")
        return [PickupStore(**store) for store in response["pickup_stores"]]

    def get_pickup_store_details(
        self, store: int | PickupStoreCreateResponse
    ) -> PickupStore:
        """Get pickup store details

        Args:
            store (int | PickupStoreCreateResponse): Store ID or PickupStoreCreateResponse object

        Returns:
            PickupStore: Pickup store details
        """
        store_id = store.id if isinstance(store, PickupStoreCreateResponse) else store
        response = self._perform_request("GET", f"pickup/store/info/{store_id}")
        return PickupStore(**response["pickup_store"])
