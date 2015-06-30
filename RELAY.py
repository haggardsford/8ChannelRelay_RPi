#!/usr/bin/python
import RPi.GPIO as GPIO
global pinList
pinList = [2,3,4,17,27,22,10,9]

def switchOn(relay):
    if relay.isOn() == False:
	relay.switchRelay()
    else: return False

def switchOff(relay):
    if relay.isOn() == True:
	relay.switchRelay()
    else: return False

def pinInit():
   GPIO.setmode(GPIO.BCM)    #init PIN mode
   for i in range(len(pinList)):
   	GPIO.setup(pinList[i], GPIO.OUT, initial=GPIO.HIGH) 

class Relay:
   
    def __init__(self, relay):
        self.relay = relay - 1   
    
    def isOn(self):
    	if GPIO.input(pinList[self.relay]) == 1:
            return False
    	else: return True

    def switchRelay(self):
       	
    	GPIO.output(pinList[self.relay], not GPIO.input(pinList[self.relay]))
              

    	
