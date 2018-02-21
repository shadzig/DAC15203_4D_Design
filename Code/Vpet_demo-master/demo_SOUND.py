# Button serving script: runs repeatedly
from datetime import datetime
import time
import sys
import RPi.GPIO as GPIO


# Sound trigger library content
from gpiozero import OutputDevice
from time import sleep


def hello():

    out= OutputDevice(26,False)


    out.on()
    sleep(0.126)
    out.toggle()
            
def snore():
    
    out= OutputDevice(19,False)


    out.on()
    sleep(0.126)
    out.toggle()
            
def whine():
    
    out= OutputDevice(13,False)


    out.on()
    sleep(0.126)
    out.toggle()
            
def grunt():
    
    out= OutputDevice(6,False)


    out.on()
    sleep(0.126)
    out.toggle()
    
def sound(m):
    if m == 1:
        hello()
        
    elif m == 2:
        snore()
        
    elif m == 3:
        whine()
        
    else:
        grunt()
    print (m)
        
