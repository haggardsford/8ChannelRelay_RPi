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

def set_Cycletime(time):
    cycletime = time
    return cycletime

def get_Cycletime():
    return cycletime

def getonofftime(cycletime, dutycycle):
    duty = duty_cycle/100.0
    on_time = cycle_time*(duty)
    off_time = cycle_time*(1.0-duty)   
    return [on_time, off_time]
    

def get_setPoint():
    return setpoint

def get_Heat_Output(temp):
    heat_output = temp_controller(temp)
    if heat_output < 0: 
        return 0 
    elif heat_output > 100:   
        return 100 
    else: return heat_output   

def PID_Process(relay):
    if !relay.isOn():
        temp = get_ctemp()
        activetime = get_Heat_Output(temp)
        cycletime = get_Cycletime()
        dutycycle = (activetime/cycletime) * 100
        if duty_cycle == 0:
            time.sleep(cycle_time)
        elif duty_cycle == 100:
            relay.switchOn()
            time.sleep(cycle_time)
        else:
            on_time, off_time = getonofftime(cycletime, dutycycle)
            relay.switchOn()
            time.sleep(on_time)
            relay.switchOff()
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
        PID_Process(heatR)    
    '''cooling logic'''
    
    '''humidity logic'''
    
    '''light logic'''
    
    
    

    
if __name__ = '__main__':
    main()

