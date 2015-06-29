# -*- coding: utf-8 -*-
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

pinList = [2,3,4,17,27,22,10,9]
def __init__(self):
    import RPi.GPIO as GPIO   
    self.pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# <codecell>


def pinInit():
    GPIO.setmode(GPIO.BCM)    #init PIN mode
    pinList = [2, 3, 4, 17, 27, 22, 10, 9]  # init list with pin numbers
    for i in range(8):                      # set all relay pins as OUTPUTS
        GPIO.setup(pinList[i], GPIO.OUT, initial=GPIO.HIGH) 

# <codecell>

def isON(relay):
    relay = relay - 1
    if GPIO.input(pinList[relay]) ==1:
        return False
    else: return True

# <codecell>

def switchOFF(relay):
    if isON(relay) == True: switchRelay(relay)
    else: 
        return False  #ALREADY OFF

# <codecell>

def switchON(relay):
    if isON(relay) == False: switchRelay(relay)
    else: return False #ALREADY ON

# <codecell>


def switchRelay(relay):
    pinList = [2,3,4,17,27,22,10,9]   
    relay = relay - 1
    GPIO.output(pinList[relay], not GPIO.input(pinList[relay]))
            

