#Script that pulls latest temp and humidity data from the dht.db sensordata table 
#to be used to drive relays On or OFF

#Relay 1 Lights
#Relay 2 Heat
#Relay 3 Humidity
#Relay 4 Cooling
import relay as R
import pid
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
    
    #name should be heat, cool, or hum. relay is the relay name ie heatR, humR, etc.
    def __init__(self, name, relay, P, I, D, cycletime, setPoint):
        self.P = P
        self.I = I
        self.D = D
        self.name= name
        self.relay = relay
        self.cycletime = cycletime
        self.setPoint = setPoint
        name = PID(P, I, D)
    
         
    def set_pid(self, name, P, I, D):
        self.name = PID(self.P, self.I, self.D)
    
    def get_cycleTime(self):
        return self.cycletime
    
    def set_cycleTime(self, time):
        self.cycletime = time
      
    def get_setPoint(self):
        return self.setPoint
        
    def set_setPoint(self, setPoint):
        self.setPoint = setPoint
        self.name.setpoint(self.setPoint)
   
    def get_activeTime(self):
        activetime = (get_Output(get_Value())/100)*get_cycleTime()
        return activetime
    def get_dutyTime(self):
        dutytime = (self.get_activeTime() / self.get_cycleTime() ) * 100
        return dutytime
    
    def getonofftime(self):
        duty = get_dutyTime()/100.0
        on_time = get_cycleTime()*(duty)
        off_time = get_cycleTime()*(1.0-duty)   
        return [on_time, off_time]
        
    def get_Output(self, name, temp):
        output = self.name.update(temp)
        if output < 0: 
            return 0 
        elif output > 100:   
            return 100 
        else: return output
    
    def get_Value(self):
        if (self.name is heat) or (self.name is cool):
            value = get_ctemp()
        else: 
            value = get_chum()
        return value
    
    def start_pid(self):
        while True:
            if !self.relay.is_on():          
                value = get_Value()
                activetime = self.get_Activetime()
                cycletime = self.get_Cycletime()
                dutycycle = self.get_Dutytime()
                if duty_cycle == 0:
                    time.sleep(cycle_time)
                elif duty_cycle == 100:
                    relay.switchOn()
                    time.sleep(cycle_time)
                else:
                    on_time, off_time = getonofftime()
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
    

    '''heat logic'''
    heatpid = PID_Process(heat, heatR, 1, 0.3, 0.1, 100, 78)    
    heat_pid.start()
    '''cooling logic'''
    
    '''humidity logic'''
    
    '''light logic'''
    
    
    

    
if __name__ = '__main__':
    main()

