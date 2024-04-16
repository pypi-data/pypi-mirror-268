import unittest
import os
from redxclient import RedXAPIClient
from pprint import pprint
from pydantic import ValidationError


class TestAreasAPI(unittest.TestCase):
    def setUp(self):
        API_KEY = os.environ.get("REDX_API_KEY")
        if not API_KEY:
            raise ValueError("API_KEY is not set")
        self.client = RedXAPIClient(API_KEY)

    def test_get_areas(self):
        areas = self.client.get_areas()
        self.assertGreater(len(areas), 0)

    def test_mutual_exclusivity_in_area_filter(self):
        with self.assertRaises(ValidationError):
            self.client.get_areas({"zone_id": 1, "post_code": 1234})
        with self.assertRaises(ValidationError):
            self.client.get_areas({"zone_id": 1, "name": "Dhaka"})
        with self.assertRaises(ValidationError):
            self.client.get_areas({"post_code": 1234, "name": "Dhaka"})

    def test_get_areas_with_filters(self):
        areas = self.client.get_areas({"zone_id": 1})
        self.assertGreater(len(areas), 0)
        for area in areas:
            self.assertEqual(area.zone_id, 1)

        areas = self.client.get_areas({"post_code": 1212})
        self.assertGreater(len(areas), 0)
        for area in areas:
            self.assertEqual(area.post_code, 1212)
