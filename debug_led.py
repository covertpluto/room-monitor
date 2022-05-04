from gpiozero import PWMLED
import time

red = PWMLED(23)
green = PWMLED(22)
blue = PWMLED(24)
blink_time = 0.5


def blink(r, g, b, duration):
    r /= 255
    g /= 255
    b /= 255
    red.value = r
    green.value = g
    blue.value = b
    time.sleep(duration)
    red.value = 0
    green.value = 0
    blue.value = 0


def nonfatal_warning():
    blink(200, 100, 0, 0.5)


def fatal_warning():
    blink(255, 0, 0, 0.5)

def success():
    blink(0, 100, 0, 0.5)

def notify():
    blink(0, 0, 255, 0.5)

def page_access_error():
    blink(255, 0, 255, 0.5)

def waiting():
    for i in range(3):
        blink(10, 0, 0, 0.1)
        blink(0, 10, 0, 0.1)
        blink(0, 0, 10, 0.1)




waiting()
