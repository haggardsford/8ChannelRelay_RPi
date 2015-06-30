#!/usr/bin/python
import RPi.GPIO as GPIO
global pinList  
pinList = [2,3,4,17,27,22,10,9]                #list of pins used for switching relays(using 8-channel relay board)

def pinInit():                   
   GPIO.setmode(GPIO.BCM)                       #sets GPIO to BCM mode
   for i in range(len(pinList)):                #initializes all pins in pinList to outputs, HIGH = relay off
       GPIO.setup(pinList[i], GPIO.OUT, \
       initial=GPIO.HIGH) 

def switchOn(relay):                             # switches relay on if off, otherwise returns False
    if relay.is_on() == False:
        relay.switch_relay()
    else: return False

def switchOff(relay):                            # switches relay off if on, otherwise returns false
    if relay.is_on() == True:
    	relay.switch_relay()
    else: return False



class Relay:
   
    def __init__(self, relay):                   #set relay 1-8 to i in pinList 0-7, so there isn't a relay 0  
        self.relay = relay - 1   
        
    def is_on(self):                              #checks whether a relay is on, returns True or False
    	if GPIO.input(pinList[self.relay]) == 1:
            return False
    	else: return True

    def switch_relay(self):                       #switches relay state
       	
    	GPIO.output(pinList[self.relay],\
    	not GPIO.input(pinList[self.relay]))
              

    	
