from gpiozero import LED
import RPi.GPIO as GPIO
import time
import debug_led

IDLE_TIMEOUT = 5 # in seconds

pirpin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirpin, GPIO.IN)

idle_start = time.time()

def check_idle():
    if time.time() - idle_start > IDLE_TIMEOUT:
        print("Idle timer passed")
        debug_led.blink(1, 0, 0, 0.5)
        return 1
    else:
        time.sleep(0.1)
        print("idle timer at", time.time() - idle_start)
        return 0

def set_timer(n):
    global idle_start
    print("You moved. Resetting idle timer...")
    idle_start = time.time()

GPIO.add_event_detect(pirpin, GPIO.BOTH, callback=set_timer, bouncetime=300)
