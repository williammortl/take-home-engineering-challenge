# --------------------------------------------------------------------------------------------------------------------
# <copyright file="geo_query_request_processor.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
from request_processor import RequestProcessor
import sqlite3
from sqlite3 import Error
import sys

# JSON signature for a query:
# ---------------------------
#
# {
# 	"Latitude": -123.4,
#   "Longitude": 432.1
# }
#
# JSON signature for a response:
# ------------------------------
#
# {
#       "Foodtrucks": [
#          {
#               "Name": "Pipo's Grill",
#               "Address": "1800 FOLSOM ST",
#               "Menu": "Tacos, Burritos, Hot Dogs, and Hamburgers",
#               "Latitude": -123.4,
#               "Longitude": 432.1,
#               "Hours": "Mo - Su: 10AM - 7PM"
#           },
#           ...
#       ]
# }

class GeoQueryRequestProcessor(RequestProcessor):

    def __init__(self, config, logger):
        super().__init__(config, logger)
        self.processorName = "geo_query"

    def requestHandler(self, req):
        latitude = req["Latitude"]
        longitude = req["Longitude"]

        # log where the geo request was for
        self.logger.logInfo("GeoRequest", "%s,%s" % (str(latitude), str(longitude)), "GeoQueryRequestProcessor::requestHandler")

        return {"Foodtrucks": self.select_foodtrucks(latitude, longitude)}

    def select_foodtrucks(self, latitude, longitude):
        sql = '''SELECT truckName, truckAddress, menu, latitude, longitude, hoursOfOp,
                ((latitude - ?)*(latitude - ?)) + ((longitude - ?)*(longitude - ?)) as distance
                FROM Trucks ORDER BY distance ASC LIMIT 5'''

        retData = []
        with self.createConnection() as conn:
            cur = conn.cursor()
            cur.execute(sql, (str(latitude), str(latitude), str(longitude), str(longitude)))
            rows = cur.fetchall()
            for row in rows:
                retData.append({"Name": row[0], "Address": row[1], "Menu": row[2], "Latitude": float(row[3]), "Longitude": float(row[4]), "Hours": row[5]})

        return retData

    def createConnection(self):
        try:
            conn = sqlite3.connect(self.config["databaseFile"])
            return conn
        except Error as e:
            print(e)

        return None