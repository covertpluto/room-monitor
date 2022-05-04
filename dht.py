import Adafruit_DHT
import debug_led
import hldetect

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17
lt = 0
lh = 0

debug_led.waiting()

def hum():
    global lt, lh
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    try:
        humidity, temperature = round(humidity, 0), round(temperature, 1)  # round it
    except TypeError:
        humidity, temperature = None, None

    if humidity is not None and temperature is not None:
        lh = humidity
        lt = temperature
        return humidity
    else:
        return lh  # in this case, the read from the sensor has failed so will return the previous values.


def temp():
    global lt, lh
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    try:
        humidity, temperature = round(humidity, 0), round(temperature, 1)  # round it
    except TypeError:
        humidity, temperature = None, None

    if humidity is not None and temperature is not None:
        lh = humidity
        lt = temperature
        hldetect.possible(lt)
        return temperature
    else:
        return lt  # in this case, the read from the sensor has failed so will return the previous values.
