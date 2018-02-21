from datetime import datetime
import time
import sys
import RPi.GPIO as GPIO

import demo_LED
import demo_SOUND


mode = 0

def modeReset():
    global mode
    mode = 4
    

def changeMode():
    global mode
    mode = mode + 1
    if mode == 5:
        mode = 1
        
    return mode
      
    
''' 
    demo_SOUND.hello()
    demo_LED.mode_smile()
    time.sleep(30):
        if mode_1 = 2:'''
            
                                    
