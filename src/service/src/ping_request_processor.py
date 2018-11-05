# --------------------------------------------------------------------------------------------------------------------
# <copyright file="ping_request_processor.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
from datetime import datetime
from request_processor import RequestProcessor
import sys

class PingRequestProcessor(RequestProcessor):

    def __init__(self, config, logger):
        super().__init__(config, logger)
        self.processorName = "ping"

    def requestHandler(self, req):
        return {"Message": "Pong", "MyUtcTime": str(datetime.now())}