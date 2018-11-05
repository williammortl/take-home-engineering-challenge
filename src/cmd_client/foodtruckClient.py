# --------------------------------------------------------------------------------------------------------------------
# <copyright file="foodtruckClient.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
import json
import requests
import sys
import warnings

URL = "https://192.168.1.210/GeoQuery"
HEADER = { "content-type": "application/json", "x-api-key": "abb378be-2863-49ee-9081-d67496f8220c"}

def printTruck(truck):
    print("Name: %s" % truck["Name"])
    print("Address: %s" % truck["Address"])
    print("Hours: %s" % truck["Hours"])
    print("Menu:\n  %s" % truck["Menu"])
    print("")

def queryServer(latitude, longitude):
    try:
        data = {"Latitude": float(latitude), "Longitude": float(longitude)}
        trucks = json.loads(requests.post(URL, data=json.dumps(data), headers=HEADER, verify=False).text)["Foodtrucks"]
        print("The 5 closest food trucks to (%s, %s) are:\n" % (latitude, longitude))
        for truck in trucks:
            printTruck(truck)
    except Exception as e:
        print("An error ocurred when connecting to the foodtruck service")

def printUsage():
    print("Usage: python3 foodtruckClient.py {lat} {long}")
    print("Example: python3 foodtruckClient.py 37.80241 -122.4059")

#
# Main function
#
if __name__ == "__main__":
    if (len(sys.argv) < 3):
        printUsage()
    else:
        warnings.simplefilter("ignore")
        queryServer(float(sys.argv[1]), float(sys.argv[2]))