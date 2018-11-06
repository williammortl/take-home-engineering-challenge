# --------------------------------------------------------------------------------------------------------------------
# <copyright file="foodtruck.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
import json
import requests
import sys
import warnings

URL = "https://127.0.0.1/GeoQuery"
XAPIKEY = "abb378be-2863-49ee-9081-d67496f8220c"

def printTruck(truck):
    print("Name: %s" % truck["Name"])
    print("Address: %s" % truck["Address"])
    print("Hours: %s" % truck["Hours"])
    print("Menu:\n  %s" % truck["Menu"])
    print("")

def queryServer(latitude, longitude, url = URL, xApiKey = XAPIKEY):
    header = { "content-type": "application/json", "x-api-key": xApiKey}
    try:
        data = {"Latitude": float(latitude), "Longitude": float(longitude)}
        trucks = json.loads(requests.post(url, data=json.dumps(data), headers=header, verify=False).text)["Foodtrucks"]
        print("The 5 closest food trucks to (%s, %s) are:\n" % (latitude, longitude))
        for truck in trucks:
            printTruck(truck)
    except Exception as e:
        print("An error ocurred when connecting to the foodtruck service")

def printUsage():
    print("Usage: python3 foodtruck.py {lat} {long} {optional: URL} {optional: XApiKey}")
    print("Example: python3 foodtruck.py 37.80241 -122.4059")

if __name__ == "__main__":
    warnings.simplefilter("ignore")
    totalArgs = len(sys.argv)
    if (totalArgs == 3):
        queryServer(float(sys.argv[1]), float(sys.argv[2]))
    elif (totalArgs == 4):
        queryServer(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3])
    elif (totalArgs == 5):
        queryServer(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4])
    else:
        printUsage()