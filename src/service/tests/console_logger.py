# --------------------------------------------------------------------------------------------------------------------
# <copyright file="console_logger.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
from datetime import datetime
import sys
import time

# constants
DEFAULT_LOCATION = "general"

class ConsoleLogger:

    def __init__(self):
        print("Debug logger starting...")

    def logTrace(self, messageName, message, location = DEFAULT_LOCATION):
        print("[%s] [%s] TRACE: %s - %s" % 
            (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), location, messageName, message))

    def logInfo(self, messageName, message, location = DEFAULT_LOCATION):
        print("[%s] [%s] INFO: %s - %s" % 
            (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), location, messageName, message))

    def logDuration(self, messageName, message, milliseconds, location = DEFAULT_LOCATION):
        print("[%s] [%s] DURATION: %s - %s :: %s milliseconds" % 
            (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), location, messageName, message, str(milliseconds)))

    def logWarning(self, messageName, message, location = DEFAULT_LOCATION):
        print("[%s] [%s] WARN: %s - %s" % 
            (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), location, messageName, message))

    def logError(self, errorClass, errorMessage, location = DEFAULT_LOCATION):
        print("[%s] [%s] ERROR: %s - %s" % 
            (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), location, errorClass, errorMessage))
