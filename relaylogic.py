#Script that pulls latest temp and humidity data from the dht.db sensordata table 
#to be used to drive relays On or OFF

#Relay 1 Lights
#Relay 2 Heat
#Relay 3 Humidity
#Relay 4 Cooling
import sqlite3
import relay as R
import pid
from datetime import datetime
from time import sleep

    #connect to database, create cursor
def get_cdata():
    db = sqlite3.connect('dht.db')
    c = db.cursor()
    c.execute('''SELECT * FROM sensordata ORDER BY id DESC LIMIT 1''')
    cdata = c.fetchone()
    return cdata
#get current temperature
def get_ctemp(): 
    cdata = get_cdata() 
    ctemp = cdata[1] 
    return ctemp 
#get current humidity
def get_chum():
    cdata = get_cdata()
    chum = cdata[2]
    return chum
#get current hour (for use with scheduling lights)
def get_chour():
    now = datetime.now()
    return now.hour

def set_pid(name, P, I, D):
    name = PID(P, I, D)

def set_setPoint(name, SP):
    global setpoint
    setpoint = SP
    name.setPoint(SP)
    return SP
    
def get_setPoint():
    return setpoint

def get_Heat_Output(temp):
    heat_output = temp_controller(temp)
    if heat_output < 0: 
        return 0 
    elif heat_output > 100:   
        return 100 
    else: return heat_output   

'''TAKEN FROM RasPiBrew!!!'''
'''Edit this to work with dht and relays'''
def heat_Process(cycle_time, duty_cycle, relay):
    p = current_process()
    print 'Starting:', p.name, p.pid
    if pinNum > 0:
        GPIO.setup(pinNum, GPIO.OUT)
        while (True):
            while (conn.poll()): #get last
                cycle_time, duty_cycle = conn.recv()
            conn.send([cycle_time, duty_cycle])  
            if duty_cycle == 0:
                GPIO.output(pinNum, OFF)
                time.sleep(cycle_time)
            elif duty_cycle == 100:
                GPIO.output(pinNum, ON)
                time.sleep(cycle_time)
            else:
                on_time, off_time = getonofftime(cycle_time, duty_cycle)
                GPIO.output(pinNum, ON)
                time.sleep(on_time)
                GPIO.output(pinNum, OFF)
                time.sleep(off_time)





def main():
    R.pinInit()
    lightR = R.Relay(1)
    heatR = R.Relay(2)
    humR = R.Relay(3)
    coolR = R.Relay(4)
    

    while True:
        temp = get_ctemp()
        hum = get_chum()
        hour = get_chour()
    '''heat logic'''
        
    '''cooling logic'''
    
    '''humidity logic'''
    
    '''light logic'''
    
    
    

    
if __name__ = '__main__':
    main()

