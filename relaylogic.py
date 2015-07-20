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
class State_Process:
    #, initial == "ON" or "OFF"
    def __init__(self, relayobj, initial)
        self.relayobj = relayobj
        self.initial = initial
        if self.initial == "ON":
            if R.Relay.in_on(self.relayobj) == False:
                R.switch_On(self.relayobj)
            
        
        
    def get_initial(self):
        return self.initial == "Low"
        return self.On_Duration
        
    def get_State(self):
        return R.Relay.is_on(self.relayobj)
    
    def set_StateON(self):
        if self.get_State() == False:
            R.switch_On(self.relayobj)
        else: 
            return False
    def set_StateOFF(self):
        if self.get_State() == True:
            R.switch_Off(self.relayobj)
        else: 
            return False
            
    

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
        activetime = (self.get_Output()/100)* self.get_cycleTime()
        return activetime
    
    def get_dutyTime(self):
        dutytime = (self.get_activeTime() / self.get_cycleTime() ) * 100
        return dutytime
    
    def getonofftime(self):
        duty = self.get_dutyTime()/100.0
        on_time = self.get_cycleTime()*(duty)
        off_time = self.get_cycleTime()*(1.0-duty)   
        return [on_time, off_time]
        
    def get_Output(self):
        output = self.PIDobj.update(self.get_Value())
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
            return value
        elif (self.param == 'hum'):
            value = get_chum()
            return value
        else: 
            pass 
    
    def start_pid(self):
        while True:
            if R.Relay.is_on(self.relayobj) == False:        
                dutycycle = self.get_dutyTime()
                if dutycycle == 0:
                    sleep(cycle_time)
                elif dutycycle == 100:
                    R.switchOn(self.relayobj)
                    sleep(cycle_time)
                else:
                    on_time, off_time = self.getonofftime()
                    R.switchOn(self.relayobj)
                    sleep(on_time)
                    R.switchOff(self.relayobj)
                    sleep(off_time)





def main():
    R.pinInit()              
    lightR = R.Relay(1)                                              
    heatR = R.Relay(2)                                             
    humR = R.Relay(3)                                             
    coolR = R.Relay(4)                                           
    heat = PID.PID(5, 0, 0) 
    heatP = PID_Process(heat, heatR, 100, 32, "temp" )  
    print ("Heat Process param=" + heatP.param) 
    print ("Current Temp= {0} ".format(heatP.get_Value()))
    print ("PID Output= {0}" .format(heatP.get_Output())) 
    print ("HeatP Setpoint={0} ".format(heatP.get_setPoint()))
    print ("On/Off Time= {0}".format(heatP.getonofftime()))
    print ("starting PID loop")
    heatP.start_pid()
    '''cooling logic'''
    
    '''humidity logic'''
    
    '''light logic'''
    
    
    

    
if __name__ == '__main__':
    main()
'''heatPID = relaylogic.PID.PID(1.5,0,0)
   relaylogic.R.pinInit()
   heatR = relaylogic.R.Relay(1)
   heatP = relaylogic.PID_Process(heat, heatR, 100, 75)
'''   
