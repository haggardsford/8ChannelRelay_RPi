#!/usr/bin/python

import relay as R
import DHT22
import pigpio
import time

if __name__ == "__main__":
    
    INTERVAL=3

    pi = pigpio.pi()
    s = DHT22.sensor(pi, 25,)
    r = 0
    next_reading = time.time()

    while True:

        r += 1
        s.trigger()
        time.sleep(0.2)

        print("{} {} {} {:3.2f} {} {} {} {}".format(
            r, s.humidity(), s.temperature(), s.staleness(),
            s.bad_checksum(), s.short_message(), s.missing_message(),
            s.sensor_resets()))

        next_reading += INTERVAL

        time.sleep(next_reading-time.time()) # Overall INTERVAL second polling.

    s.cancel()

    pi.stop()

