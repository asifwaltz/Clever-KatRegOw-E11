import time
import board
import busio 
from digitalio import DigitalInOut, Direction, Pull

import serial
uart = serial.Serial("/dev/ttyUSB0", baudrate = 9600, timeout = 0.25)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

print("Found PM2.5 sensor, reading data :3...")

while True:
    time.sleep(1)
    
    try:
        aqdata = pm25.read()
    except RuntimeError:
        print("Unable to read from sensor you idiot. Retrying...")
        continue
        
    print()
    print("Concentration Units (standard)")
    print("----------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
        )
    print("Concentration Units (environmental)")
    print("----------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
        )
    print("----------------------------------------")
    
    print("Particles > 0.3 um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5 um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0 um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5 um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0 um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("----------------------------------------")
