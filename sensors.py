import dht
import pirsensor
import lightsensor
import hldetect

def temp():
    return dht.temp()


def hum():
    return dht.hum()


def light():
    return lightsensor.detected()


def motion():
    return pirsensor.check_idle()

def heatloss():
    return hldetect.check()