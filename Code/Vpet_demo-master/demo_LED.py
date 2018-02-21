# Button serving script: runs repeatedly
from datetime import datetime
import time
import sys
import RPi.GPIO as GPIO


# Sound trigger library content
from gpiozero import OutputDevice
from time import sleep

# Neopixel libraries
from neopixel import *

# LED strip configuration:
LED_COUNT = 17 # Number of LED pixels.
LED_PIN = 18 # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating signal (try 5)
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)

#Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)

# Strip LED Settings
smileLED = {
    'neoNumbers' : [2,3,4,5,6,7,8,9,10,11,12,13,14],
    'color' : {'g': 235,'r': 16, 'b' : 0}
}

neutralLED = {
    'neoNumbers' : [2,3,4,7,8,9,10,11,12,13,14],
    'color' : {'g': 235,'r': 235, 'b' : 0}
    
}
sadLED = {
    'neoNumbers' : [0,1,2,3,4,7,8,11,12,15,16],
    'color' : {'g': 150,'r': 235, 'b' : 0}
}

angryLED = {
    'neoNumbers' : [0,1,2,3,4,5,6,7,8,10,11,12,13,15,16],
    'color' : {'g': 16,'r': 235, 'b' : 0}
}

clearLED = {
    'neoNumbers' : [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
    'color' : {'g': 0,'r': 0, 'b' : 0}
}

strip.begin()

def mode_smile():
    
    for i in clearLED['neoNumbers']:
            strip.setPixelColorRGB(i, clearLED['color']['g'], clearLED['color']['r'], clearLED['color']['b'])
            strip.show()
            
    for i in smileLED['neoNumbers']:
            strip.setPixelColorRGB(i, smileLED['color']['g'], smileLED['color']['r'], smileLED['color']['b'])
            strip.show()
    
def mode_neutral():
    
    for i in clearLED['neoNumbers']:
            strip.setPixelColorRGB(i, clearLED['color']['g'], clearLED['color']['r'], clearLED['color']['b'])
            strip.show()
            
    for i in neutralLED['neoNumbers']:
            strip.setPixelColorRGB(i, neutralLED['color']['g'], neutralLED['color']['r'], neutralLED['color']['b'])
            strip.show()
    
def mode_sad():
    
    for i in clearLED['neoNumbers']:
            strip.setPixelColorRGB(i, clearLED['color']['g'], clearLED['color']['r'], clearLED['color']['b'])
            strip.show()
            
    for i in sadLED['neoNumbers']:
            strip.setPixelColorRGB(i, sadLED['color']['g'], sadLED['color']['r'], sadLED['color']['b'])
            strip.show()

def mode_angry():
    
    for i in clearLED['neoNumbers']:
            strip.setPixelColorRGB(i, clearLED['color']['g'], clearLED['color']['r'], clearLED['color']['b'])
            strip.show()
            
    for i in angryLED['neoNumbers']:
            strip.setPixelColorRGB(i, angryLED['color']['g'], angryLED['color']['r'], angryLED['color']['b'])
            strip.show()


def LED(m):
    if m == 1:
        mode_smile()
        
    elif m == 2:
        mode_neutral()
        
    elif m == 3:
        mode_sad()
        
    else:
        mode_angry()
    print (m)