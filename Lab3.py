import time 
import board 
import adafruit_bme680

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME_I2C(i2c, debug=False)

bme680.sea_level_pressure = 1013.25

temperature_offset = -5

now = time.time()
duration = 30
while (time.time() < now + duration):
	print("Time is: " + time.time() + "\nTemperature: %0.1f C" % (bme680.temperature + temperature_offset) + "\nGas: %d ohm" % bme680.gas + "\nHumidity: %0.1f %%" % bme680.relative_humidity + "\nPressure: %0.3f hPa" % bme680.pressure + "\nAltitude = %0.2f meters" % bme680.altitude)
	
	time.sleep(1)
