#Script that pulls latest temp and humidity data from the dht.db sensordata table 
#to be used to drive relays On or OFF

#Relay 1 Lights
#Relay 2 Heat
#Relay 3 Humidity
#Relay 4 Cooling


    #connect to database, create cursor
        db = sqlite3.connect('dht.db')
        c = db.cursor()
        data =  c.execute('''SELECT * FROM sensordata WHERE ID = (SELECT MAX(ID) FROM sensordata''')
        
        db.commit()
        db.close()

