import time
import board
import digitalio
import adafruit_bme680

cs = digitalio.DigitalInOut(board.D10)
spi = board.SPI()
bme680 = adafruit_bme680.Adafruit_BME680_SPI(spi, cs)

bme680.sea_level_pressure = 1013.25
temperature_offset = -5

i = 0
while (i <= 5):
	print("\nTemperature: %0.1f C" % (bme680.temperature + temperature_offset))
	print("Gas: %d ohm" % bme680.gas)
	print("Humidity: %0.1f %%" % bme680.relative_humidity)
	print("Pressure: %0.3f hPa" % bme680.pressure)
	print("Altitude = %0.2f meters" % bme680.altitude)
	i += 1

	
	time.sleep(1)
