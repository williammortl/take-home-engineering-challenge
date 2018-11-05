# --------------------------------------------------------------------------------------------------------------------
# <copyright file="foodtruck_service.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
from datetime import datetime
from flask import (Flask, jsonify, request, Response)
from foodtruck_service_logger import FoodtruckServiceLogger
from geo_query_request_processor import GeoQueryRequestProcessor as GQRP
import json
import os
from ping_request_processor import PingRequestProcessor as PRP
import sys
import threading

# load config and logger
_config = json.loads(open('config.json').read())
_myLogger = FoodtruckServiceLogger(_config)

# instantiate request processors
_prp = PRP(_config, _myLogger)
_gqrp = GQRP(_config, _myLogger)

# flask variables and basic handlers
app = Flask(__name__)
lock = threading.Lock()

@app.errorhandler(500)
def error_handling(error):
    errorStr = str(error)
    _myLogger.logError("error_handlingException", errorStr, "error_handling")
    res = jsonify({ "Message:": "an error occurred", "Exception": errorStr})
    res.status_code = 500
    return res

#
# Function handlers - ADD NEW HANDLERS HERE REPRODUCING THIS PATTERN
#
@app.route("/Ping", methods=["GET", "POST"])
def handlePing():
    return _prp.processIncomingRequest({})

@app.route("/GeoQuery", methods=["POST"])
def handleGeoQuery():
    return _gqrp.processIncomingRequest(request.json)

#
# Server startup
#
if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = _config["port"])