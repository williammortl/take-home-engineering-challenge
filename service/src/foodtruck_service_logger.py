# --------------------------------------------------------------------------------------------------------------------
# <copyright file="foodtruck_service_logger.py" company="Microsoft">
#   2018 William M Mortl
# </copyright>
# --------------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import
from aria import LogManager, EventProperties, PiiKind, LogConfiguration, LogManagerConfiguration
from datetime import datetime
import logging
import os
import random
import sys
import time

# constants
DEFAULT_LOCATION = "general"

# this class is used to send telemetry to aria.ms
class FoodtruckServiceLogger:
    debug = 0
    token = ""
    logger = []

    def __init__(self, config):
        self.debug = config["debug"]
        self.token = config["token"]

        # init logging
        if (self.token != ""):

            # minimum logging level
            log_config = LogConfiguration(log_level = logging.DEBUG)
            
            # create the configuraiton for LogManager
            configuration = LogManagerConfiguration(tcp_connections = 2 ,max_events_in_memory = 15000, log_configuration = log_config, drop_event_if_max_is_reached = False)
            
            # initialize logManager with the token and the configuration
            LogManager.initialize(self.token, configuration)

            # return the logger
            self.logger = LogManager.get_logger("", self.token)

            # subscribe
            LogManager.add_subscriber(update)

    def __del__(self):
        LogManager.flush(timeout = 0)

    def logTrace(self, messageName, message, location = DEFAULT_LOCATION):
        if (self.debug > 0):
            print("[%s] [%s] TRACE: %s - %s" % 
                (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), location, messageName, message))

    def logInfo(self, messageName, message, location = DEFAULT_LOCATION):
        if (self.debug > 0):
            print("[%s] [%s] INFO: %s - %s" % 
                (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), location, messageName, message))
        if (self.token != ""):
            self.sendEvent(self.createEvent(messageName, message, location, "Info"))

    def logDuration(self, messageName, message, milliseconds, location = DEFAULT_LOCATION):
        if (self.debug > 0):
            print("[%s] [%s] DURATION: %s - %s :: %s milliseconds" % 
                (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), location, messageName, message, str(milliseconds)))
        if (self.token != ""):
            event = EventProperties(messageName)
            event.set_property("Level", "Duration")
            event.set_property("Message", message)
            event.set_property("Milliseconds", milliseconds)
            event.set_property("Location", location)
            self.sendEvent(event)

    def logWarning(self, messageName, message, location = DEFAULT_LOCATION):
        if (self.debug > 0):
            print("[%s] [%s] WARN: %s - %s" % 
                (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), location, messageName, message))
        if (self.token != ""):
            self.sendEvent(self.createEvent(messageName, message, location, "Warning"))

    def logError(self, errorClass, errorMessage, location = DEFAULT_LOCATION):
        if (self.debug > 0):
            print("[%s] [%s] ERROR: %s - %s" % 
                (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), location, errorClass, errorMessage))
        if (self.token != ""):
            event = EventProperties("Error")
            event.set_property("Level", "Error")
            event.set_property("ErrorClass", errorClass)
            event.set_property("ErrorMessage", errorMessage)
            event.set_property("Location", location)
            self.sendEvent(event)  

    def sendEvent(self, event):
        eventID = self.logger.log_event(event)
        while eventID < 0:
             time.sleep(0.00001)
             eventID = self.logger.log_event(event)
        AriaResults.events_send.append(eventID)

    @staticmethod
    def createEvent(messageName, message, location, level):
        event = EventProperties(messageName)
        event.set_property("Level", level)
        event.set_property("Message", message)
        event.set_property("Location", location)
        return event

class AriaResults(object):
    events_send = []
    events_received_callback = 0
    result_map = {}

def update(tenant, sequence_list, result):
    if result not in AriaResults.result_map:
        AriaResults.result_map[result] = 0
        
    AriaResults.result_map[result] += len(sequence_list)
    AriaResults.events_received_callback += len(sequence_list)

    for i in sequence_list:
        AriaResults.events_send.remove(i)

