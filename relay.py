#!/usr/bin/python
import RPi.GPIO as GPIO
global pinList
pinList = (2, 3, 4, 17, 27, 22, 10, 9)
def set_pinList(*args):                         #sets pinList, the list of pins to be initialized for use as relays
    global pinList                              #pinList should be between 1 and 8 ints long, ex:(1) - (1,2,3,4,5,6,7,8) BCM pin numbering  
    pinList = args 

def pinInit():                   
   GPIO.setmode(GPIO.BCM)                       #sets GPIO to BCM mode
   for i in pinList:                #initializes all pins in pinList to outputs, HIGH = relay off
       GPIO.setup(i, GPIO.OUT, \
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
              

    	
