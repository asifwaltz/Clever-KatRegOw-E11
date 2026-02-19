import time
import board
import busio 
from digitalio import DigitalInOut, Direction, Pull
import csv
import numpy as np
import sys
import adafruit_bme680


i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME_I2C(i2c, debug=False)
bme680.sea_level_pressure = 1013.25
temperature_offset = -5

args = sys.argv
dataPath = "data/" + args[1]
runtime = int(args[2])

file = open(dataPath, "w", newline = None)
csvwrt = csv.writer(file, delimiter = ",")

meta = ["time", "temp", "gas", "humidity", "pressure", "alt", "stndr10", "stndr25", "stndr100", "enviro10", "enviro25", "enviro100", "p03um", "p05um", "p10um", "p25um", "p50um", "p100um"]
csvwrt.writerow(meta)

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

from adafruit_pm25.uart import PM25_UART
reset_pin = None
pm25 = PM25_UART(uart, reset_pin)

print("Found PM2.5 sensor, reading data :3...")

now = time.time()
while (time.time() < now + runtime):
    time.sleep(1)
    
    try:
        aqdata = pm25.read()
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue


    print(f"\nTime: {time.ctime()}s")
    print()
    print("\nTemperature: %0.1f C" % (bme680.temperature + temperature_offset))
    print("\nTemperature: %0.1f C" % (bme680.temperature + temperature_offset))
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.relative_humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)
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

    csvwrt.writerow([nownow, bme680.temperature + temperature_offset, bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude, aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"], aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"],aqdata["particles 03um"], aqdata["particles 05um"], aqdata["particles 10um"], aqdata["particles 25um"], aqdata["particles 50um"], aqdata["particles 100um"]])

for i in range(runtime):
    nownow = time.time()
    csvwrt.writerow([nownow, bme680.temperature + temperature_offset, bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude, aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"], aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"],aqdata["particles 03um"], aqdata["particles 05um"], aqdata["particles 10um"], aqdata["particles 25um"], aqdata["particles 50um"], aqdata["particles 100um"]])

file.close()
