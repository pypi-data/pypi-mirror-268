import os
import unittest

from redxclient import RedXAPIClient


class TestStoresAPI(unittest.TestCase):
    def setUp(self):
        API_KEY = os.environ.get("REDX_API_KEY")
        if not API_KEY:
            raise ValueError("API_KEY is not set")
        self.client = RedXAPIClient(API_KEY)
        areas = self.client.get_areas()
        self.area = areas[0]
        self.store_create_data = {
            "name": "Test Store",
            "address": "Test Address",
            "phone": "01700000000",
            "email": "testuser@testdomain.com",
            "area_id": self.area.id
            }

    def test_create_store(self):
        store = self.client.create_pickup_store(self.store_create_data)
        self.assertIsNotNone(store.id)

    def test_get_stores(self):
        self.client.create_pickup_store(self.store_create_data)
        stores = self.client.get_pickup_stores()
        self.assertGreater(len(stores), 0)

    def test_get_store_details(self):
        store = self.client.create_pickup_store(self.store_create_data)
        store_id = store.id
        store = self.client.get_pickup_store_details(store_id)
        self.assertEqual(store.id, store_id)
