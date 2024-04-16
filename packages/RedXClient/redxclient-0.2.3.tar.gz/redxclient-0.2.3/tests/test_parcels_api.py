import os
import unittest

from redxclient import RedXAPIClient


class TestParcelsAPI(unittest.TestCase):
    def setUp(self):
        API_KEY = os.environ.get("REDX_API_KEY")
        if not API_KEY:
            raise ValueError("API_KEY is not set")
        self.client = RedXAPIClient(API_KEY)
        self.area = self.client.get_areas()[0]
        self.parcel_create_data = {
            "customer_name": "Test Customer",
            "customer_phone": "01700000000",
            "customer_address": "Test Address, Badda, Dhaka",
            "delivery_area_id": self.area.id,
            "delivery_area": self.area.name,
            "instruction": "Handle with care",
            "parcel_weight": 700,
            "value": 1000,
            "cash_collection_amount": "1000",
            "is_closed_box": True,
            "parcel_details_json": [
                {
                    "name": "Test Product",
                    "category": "Test Category",
                    "value": 1000.0,
                }
            ]
        }

    def test_create_parcel(self):
        tracking_id = self.client.create_parcel(self.parcel_create_data)
        self.assertIsNotNone(tracking_id)

    def test_get_parcel_details(self):
        tracking_id = self.client.create_parcel(self.parcel_create_data)
        parcel = self.client.get_parcel_details(tracking_id)
        self.assertEqual(parcel.tracking_id, tracking_id)

    def test_track_percel(self):
        tracking_id = self.client.create_parcel(self.parcel_create_data)
        tracking = self.client.track_percel(tracking_id)
        self.assertGreater(len(tracking), 0)
