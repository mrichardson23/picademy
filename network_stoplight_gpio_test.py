from RPi import GPIO
from time import sleep

# Set up GPIO:
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
RED = 15
YELLOW = 18
GREEN = 14
ALL = [RED, YELLOW, GREEN]
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

# Test the traffic light by binking all lights, then one at a time:

while True:
    GPIO.output(ALL, True)
    sleep(1)
    GPIO.output(ALL, False)
    sleep(1)
    for light in ALL:
        GPIO.output(light, True)
        sleep(1)
        GPIO.output(light, False)
    GPIO.output(ALL, False)
    sleep(1)
