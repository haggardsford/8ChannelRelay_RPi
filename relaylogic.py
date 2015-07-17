#Script that pulls latest temp and humidity data from the dht.db sensordata table 
#to be used to drive relays On or OFF
#TESTTESTTEST Push to GIT
#Relay 1 Lights
#Relay 2 Heat
#Relay 3 Humidity
#Relay 4 Cooling
import relay as R
import PID
import sqlite3
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


#make a PID_Process object for each PID process
class PID_Process:
    
    #name should be heat, cool, or hum. relay is the relay name ie heatR, humR, etc., param== 'temp' or 'hum'
    def __init__(self, PIDobj, relayobj, cycletime, setPoint, param):
        self.setPoint = setPoint
        self.PIDobj = PIDobj
        self.relayobj = relayobj
        self.cycletime = cycletime
        self.PIDobj.setpoint(setPoint)
        self.param = param
        
    def get_cycleTime(self):
        return self.cycletime
    
    def set_cycleTime(self, time):
        self.cycletime = time
      
    def get_setPoint(self):     #might now work
        return self.PIDobj.set_point
        
    def set_setPoint(self, setPoint): #might not work
        self.setPoint = setPoint
        self.PIDobj.setpoint(setPoint)
   
    def get_activeTime(self):
        activetime = (get_Output()/100)*get_cycleTime()
        return activetime
    
    def get_dutyTime(self):
        dutytime = (self.get_activeTime() / self.get_cycleTime() ) * 100
        return dutytime
    
    def getonofftime(self):
        duty = get_dutyTime()/100.0
        on_time = get_cycleTime()*(duty)
        off_time = get_cycleTime()*(1.0-duty)   
        return [on_time, off_time]
        
    def get_Output(self):
        output = self.PIDobj.update(get_Value())
        if output < 0: 
            result = 0
            return result
        elif output > 100:   
            result = 100
            return result
        else: return output
    
    def get_Value(self):
        if (self.param  == 'temp'):
            value = get_ctemp()
        elif (self.param == 'hum'): 
            value = get_chum()
        return value
    
    def start_pid(self):
        while True:
            if R.Relay.is_on(self.relayobj) == False:        
                activetime = self.get_Activetime()
                cycletime = self.get_Cycletime()
                dutycycle = self.get_Dutytime()
                if duty_cycle == 0:
                    time.sleep(cycle_time)
                elif duty_cycle == 100:
                    R.switchOn(self.relayobj)
                    time.sleep(cycle_time)
                else:
                    on_time, off_time = getonofftime()
                    R.switchOn(self.relayobj)
                    time.sleep(on_time)
                    R.switchOff(self.relayobj)
                    time.sleep(off_time)





def main():
    R.pinInit()
    lightR = R.Relay(1)
    heatR = R.Relay(2)
    humR = R.Relay(3)
    coolR = R.Relay(4)
    

    '''heat logic'''
    heat = PID(1, 0, 0)
    heatP = PID_Process(heat, heatR, 5, 82)    
    heat_pid.start()
    '''cooling logic'''
    
    '''humidity logic'''
    
    '''light logic'''
    
    
    

    
if __name__ == '__main__':
    main()
'''heatPID = relaylogic.PID.PID(1.5,0,0)
   relaylogic.R.pinInit()
   heatR = relaylogic.R.Relay(1)
   heatP = relaylogic.PID_Process(heat, heatR, 5, 75)
   
