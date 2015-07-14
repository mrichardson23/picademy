from RPi import GPIO
from time import sleep
from pubnub import Pubnub
import credentials


# Set up GPIO:
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BUTTON = 4

# Set up PubNub
pubnub = Pubnub(publish_key=credentials.PUBNUB_PUBLISH_KEY, subscribe_key=credentials.PUBNUB_SUBSCRIBE_KEY, uuid='CONTROLLER')


GPIO.setup(BUTTON, GPIO.IN, GPIO.PUD_UP)


while True:
    GPIO.wait_for_edge(BUTTON, GPIO.FALLING)
    message = {'text' : "GREEN"}
    pubnub.publish('traffic_light', message)
    sleep(.5)
    GPIO.wait_for_edge(BUTTON, GPIO.FALLING)
    message = {'text' : "YELLOW"}
    pubnub.publish('traffic_light', message)
    sleep(.5)
    GPIO.wait_for_edge(BUTTON, GPIO.FALLING)
    message = {'text' : "RED"}
    pubnub.publish('traffic_light', message)
    sleep(.5)
    GPIO.wait_for_edge(BUTTON, GPIO.FALLING)
    message = {'text' : "OFF"}
    pubnub.publish('traffic_light', message)
    sleep(.5)

    
