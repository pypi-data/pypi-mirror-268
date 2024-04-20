#
# Este modulo es un simple timer, que coloc un evento con paramtros despues de 
# del tiempo indicado
#
import re
import threading
import os.path
import traceback
from .logger import Logger
from time import sleep
from .smallneuron import  EventManager

log=Logger("smallneuron.SnTimer")

class SnTimer():
    def __init__(self, eventManager:EventManager):
        self.eventManager = eventManager
        log.info("start")

    # Los eventos agregado con timer son por defecto 
    # solo validos para el siguiente estado
    def putEvent(self, event, params={}, time=1.0, valid=1):
        log.debug("putEvent:", event,params,time,valid)
        if valid != None:
            params["validUntil"] = self.eventManager.count+valid

        self.eventManager.watchEvent(event=event,event_args=params,bridge=self,bridge_args={"time":time},mode="noloop")

    def check(self,time):
        sleep(time)
        return {"time": time}

    def start(self):
        print("SnTimer started")
