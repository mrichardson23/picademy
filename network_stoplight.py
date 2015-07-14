from RPi import GPIO
from time import sleep
from pubnub import Pubnub
import credentials

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
GPIO.output(ALL, False)
mode = "auto"

# Set up PubNub
pubnub = Pubnub(publish_key=credentials.PUBNUB_PUBLISH_KEY, subscribe_key=credentials.PUBNUB_SUBSCRIBE_KEY)

def _callback(message, channel):
    if message['text'] == "RED":
        GPIO.output(ALL, False)
        GPIO.output(RED, True)
    if message['text'] == "GREEN":
        GPIO.output(ALL, False)
        GPIO.output(GREEN, True)
    if message['text'] == "YELLOW":
        GPIO.output(ALL, False)
        GPIO.output(YELLOW, True)
    if message['text'] == "OFF":
        GPIO.output(ALL, False)

def _error(message):
    print(message)

pubnub.subscribe(channels="traffic_light", callback=_callback, error=_error)

while True:
    pass
