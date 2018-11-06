# --------------------------------------------------------------------------------------------------------------------
# <copyright file="procrequest_processoressor.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from datetime import datetime
from flask import (jsonify, request, Response)
import json
import traceback

MISSING = "N/A" 

class RequestProcessor(ABC):

    config = []
    logger = []
    processorName = MISSING

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        super().__init__()

    def processIncomingRequest(self, req):
        start = datetime.now()
        try:
            res = jsonify(self.requestHandler(req))

        except Exception as e:
            errorMessage = "Exception: %s\r\nStack trace:%s\r\nRequest:%s" % (str(e), traceback.extract_stack(), str(req))
            self.logger.logError("baseHandlerException", errorMessage, self.processorName)
            res = jsonify({ "Message": "Error in %s" % self.processorName, "Exception": str(e)})
            res.status_code = 500

        finally:
            end = datetime.now()
            timeDiff = end - start
            milliseconds = timeDiff.total_seconds() * 1000
            self.logger.logDuration("ProcessedRequest", "completed", milliseconds, self.processorName)
        
        return res

    @abstractmethod
    def requestHandler(self, req):
        pass