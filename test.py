import time 
import board 
import adafruit_bme680

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME_I2C(i2c, debug=False)

bme680.sea_level_pressure = 1013.25

temperature_offset = -5

while True:
	print("\nTemperature: %0.1f C" % (bme680.temperature + temperature_offset))
	print("Gas: %d ohm" % bme680.gas)
	print("Humidity: %0.1f %%" % bme680.relative_humidity)
	print("Pressure: %0.3f hPa" % bme680.pressure)
	print("Altitude = %0.2f meters" % bme680.altitude)
	
	time.sleep(1)
