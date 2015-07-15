#Script that pulls latest temp and humidity data from the dht.db sensordata table 
#to be used to drive relays On or OFF

#Relay 1 Lights
#Relay 2 Heat
#Relay 3 Humidity
#Relay 4 Cooling
import sqlite3

    #connect to database, create cursor
def get_cdata():
    db = sqlite3.connect('dht.db')
    c = db.cursor()
    c.execute('''SELECT * FROM sensordata ORDER BY id DESC LIMIT 1''')
    cdata = c.fetchone()
    return cdata

def main():
    ctemp, chum = get_cdata()
    
    '''heat logic'''
    
    '''cooling logic'''
    
    '''humidity logic'''
    
    '''light logic'''
    
    
    

    
if __name__ = '__main__':
    main()

