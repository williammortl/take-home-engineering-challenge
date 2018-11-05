# --------------------------------------------------------------------------------------------------------------------
# <copyright file="test_geo_query_request_processor.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
from console_logger import ConsoleLogger
from geo_query_request_processor import GeoQueryRequestProcessor as GQRP
import math
import os
import sys
import unittest

# unit test class
class Test_GeoQueryRequestProcessor(unittest.TestCase):

    config = {"databaseFile": "truck.db"}
    logger = ConsoleLogger()
    gqrp = GQRP(config, logger)

    def test_coit_tower_foodtrucks(self):
        req = {"Latitude": 37.80241, "Longitude": -122.4059} # this is actually Coit Tower!
        self.logger.logTrace("Test starting", str(req), "Test_GeoQueryRequestProcessor::test_coit_tower_foodtrucks")
        response = self.gqrp.requestHandler(req)
        self.assertEqual("Mike's Catering", response["Foodtrucks"][0]["Name"])
        self.assertEqual("Philz Coffee Truck", response["Foodtrucks"][1]["Name"])
        self.assertEqual("Akuranvyka USA Inc", response["Foodtrucks"][2]["Name"])
        self.assertEqual("M M Catering", response["Foodtrucks"][3]["Name"])
        self.assertEqual("Wu Wei LLC dba MoBowl", response["Foodtrucks"][4]["Name"])

if __name__ == '__main__':
    unittest.main()