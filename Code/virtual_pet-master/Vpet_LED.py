
import time
from neopixel import *

import argparse
import signal
import sys

# LED strip configuration:
LED_COUNT = 17 # Number of LED pixels.
LED_PIN = 18 # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating signal (try 5)
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)
# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)

'''green = Color(0,230,0)

opt_parse()

def colorWipe(strip, color, wait_ms):
    numbOfPix = strip.numPixels()
    for i in range(numbOfPix):
        strip.setPixelColor(0, Color(0,0,0))
        print(i)
        strip.show()
        time.sleep(wait_ms/1000.0)
        
#print(green)
colorWipe(strip, green, 20)

'''

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

# Intialize the library (must be called once before other functions).

#strip.begin()
'''for i in clearLED['neoNumbers']:
    strip.setPixelColorRGB(i, clearLED['color']['g'], clearLED['color']['r'], clearLED['color']['b'])
    strip.show()'''
    

    
strip.begin()
for i in sadLED['neoNumbers']:
    strip.setPixelColorRGB(i, sadLED['color']['g'], sadLED['color']['r'], sadLED['color']['b'])
    strip.show()
    

    

'''
# Define functions which animate LEDs in various ways.
def Smile-green(strip, color, wait_ms=5000):
"""Smile animation, show smiling face."""
setPixelColorRGB((2,3,4,5,6,7,8,9,10,11,12,13,14), 16, 235, 0)
strip.show()
time.sleep(wait_ms/1000.0)


def neutral-yellow(strip, color, wait_ms=5000):
"""neutral animation, show blunt face."""
setPixelColorRGB((2,3,4,7,8,9,10,11,12,13,14), 235, 235, 0)
strip.show()
time.sleep(wait_ms/1000.0)

def sad-orange(strip, color, wait_ms=5000):
"""sad animation, show sad face."""
setPixelColorRGB((0,1,2,3,4,7,8,11,12,15,16), 235, 150, 0)
strip.show()
time.sleep(wait_ms/1000.0)

def angry-red(strip, color,  wait_ms=5000):
"""angry animation, show angry face"""
setPixelColorRGB((0,1,2,3,4,7,8,11,12,15,16), 235, 150, 0)
strip.show()
time.sleep(wait_ms/1000.0)




print 'Press Ctrl-C to quit.'
while True:
# Animations.
        print ('Smile animation, show smiling face.')
        Smile-green(strip, color):
        print ('neutral animation, show blunt face.')
        neutral-yellow(strip, color):
        print ('sad animation, show sad face.')
        sad-orange(strip, color):
        print ('angry animation, show angry face.')
        angry-red(strip, color):
'''
