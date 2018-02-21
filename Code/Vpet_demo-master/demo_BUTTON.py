import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def press():
    input_state = GPIO.input(10)
    if input_state == False:
        print("button Pressed")
    
    return not input_state
