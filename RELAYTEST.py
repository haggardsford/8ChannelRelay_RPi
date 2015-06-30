#!/usr/bin/python
import RPi.GPIO as GPIO
global pinList
pinList = [2,3,4,17,27,22,10,9]

class RelayTest:
    def __init__(self, relay):
        self.relay = relay - 1   
    def pinInit(self):
   	  
   	GPIO.setmode(GPIO.BCM)    #init PIN mode
    	GPIO.setup(pinList[self.relay], GPIO.OUT, initial=GPIO.HIGH) 

# <codecell>
    @staticmethod
    def isON(self):
    	
    	if GPIO.input(pinList[self.relay]) ==1:
            return False
    	else: return True

# <codecell>

    def switchOFF(self):
    	if self.isON(self.relay) == True: switchRelay(self.relay)
    	else: return False  #ALREADY OFF

# <codecell>

    def switchON(self):
    	if self.isON(self.relay) == False: switchRelay(self.relay)
    	else: return False #ALREADY ON

# <codecell>


    def switchRelay(self):
       	
    	GPIO.output(pinList[self.relay], not GPIO.input(pinList[self.relay]))
              
