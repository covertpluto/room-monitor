from gpiozero import LightSensor
import debug_led
import time

s = LightSensor(4, threshold=0.7)


def detected():
    if s.light_detected:
        return 1
    else:
        return 0
