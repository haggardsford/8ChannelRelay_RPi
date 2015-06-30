#!/usr/bin/python

import relay as R
import DHT22
import pigpio
import time
import sqlite3




if __name__ == "__main__":
    
    INTERVAL=3

    pi = pigpio.pi()
    s = DHT22.sensor(pi, 25,)
    r = 0
    next_reading = time.time()
    db = sqlite3.connect('dht.db')
    c = db.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS sensordata (id INTEGER PRIMARY KEY, temp REAL, hum REAL)''')
    while True:

        r += 1
        s.trigger()
        time.sleep(0.2)
        
        temp = s.temperature()
        hum = s.humidity()
        
        #Database entries
        
        db = sqlite3.connect('dht.db')
        c = db.cursor()
       
        c.execute('''CREATE TABLE sensordata (id INTEGER PRIMARY KEY, temp REAL, hum REAL)''')
        c.execute("INSERT INTO sensordata (temp, hum) VALUES (?,?)"(temp, hum)
        
        db.commit()
        db.close()
        
        #print("{} {} {} {:3.2f} {} {} {} {}".format(
        #    r, s.humidity(), s.temperature(), s.staleness(),
        #    s.bad_checksum(), s.short_message(), s.missing_message(),
        #    s.sensor_resets()))

        next_reading += INTERVAL

        time.sleep(next_reading-time.time()) # Overall INTERVAL second polling.

    s.cancel()

    pi.stop()

