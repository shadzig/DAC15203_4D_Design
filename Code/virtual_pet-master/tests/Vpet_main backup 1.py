# Button serving script: runs repeatedly
from datetime import datetime
import time
import sys
import RPi.GPIO as GPIO


# Sound trigger library content
from gpiozero import OutputDevice
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Neopixel libraries
from neopixel import *

# LED strip configuration:
LED_COUNT = 17 # Number of LED pixels.
LED_PIN = 18 # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating signal (try 5)
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)


# Create NeoPixel object with appropriate configuration.
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

# Intialize the library (must be called once before other functions).3600

# Start by reading the existing JSON file, if it exists.
IDLE_DAYTIME = 1
Smile = 2
Neutral = 3
Sad = 4
Angry = 5
BUTTON_DONE = 6

state = Smile #IDLE_DAYTIME

jsonLastWrittenTime = datetime.now()

def readJSON():
    pass

def writeJSON():
    print("writeJSON")


def sampleButton():
    print("SAMPLE")
    
    
    input_state = GPIO.input(9)
    if input_state == False:
        return 1
    else:
        return 0

def middleOfDay():
    now = datetime.now()
    hour = now.hour
    return hour > 12 and hour < 13
    strip.begin()
    
#sound time loops   
out_grunt= OutputDevice(6 ,False) #replace out with other variable
out_whine= OutputDevice(13 ,False) #replace out with other variable
out_snore= OutputDevice(19 ,False) #replace out with other variable
out_hello= OutputDevice(26 ,False) #replace out with other variable

#strip activation

strip.begin()

def stateForTime():
    # Return IDLE, Smile, Neutral, Sad, Angry LED smiley, depending on time of day:
    now = datetime.now()
    hour = now.hour

    if hour >= 20:
        
        
        # Sound "hello"
        pet_sound_repeat = datetime.now()

            now = datetime.now()
            SoundSecs = (now - pet_sound_repeat).total_seconds()

            if SoundSecs > 900:
                pet_sound_repeat = now

                out_hello.on() #replace out with other variable
                sleep(0.126)
                out_hello.toggle()

        
        # Run Neopixel "smileLED", green
        
        for i in smileLED['neoNumbers']:
            strip.setPixelColorRGB(i, smileLED['color']['g'], smileLED['color']['r'], smileLED['color']['b'])
            strip.show()
        
        for i in clearLED['neoNumbers']:
            strip.setPixelColorRGB(i, clearLED['color']['g'], clearLED['color']['r'], clearLED['color']['b'])
            strip.show()
            
        return Smile
        
    elif hour >= 21:
    
        # Sound "Snore"
        pet_sound_repeat = datetime.now()

            now = datetime.now()
            SoundSecs = (now - pet_sound_repeat).total_seconds()

            if SoundSecs > 900:
                pet_sound_repeat = now

                out_snore.on() #replace out with other variable
                sleep(0.126)
                out_snore.toggle()
        
         # Run Neopixel "neutralLED", green

        for i in neutralLED['neoNumbers']:
            strip.setPixelColorRGB(i, neutralLED['color']['g'], neutralLED['color']['r'], neutralLED['color']['b'])
            strip.show()
            
        for i in clearLED['neoNumbers']:
            strip.setPixelColorRGB(i, clearLED['color']['g'], clearLED['color']['r'], clearLED['color']['b'])
            strip.show()
            
        return Neutral
        
    elif hour >= 22:
    
        # Sound "Whine"
        pet_sound_repeat = datetime.now()

            now = datetime.now()
            SoundSecs = (now - pet_sound_repeat).total_seconds()

            if SoundSecs > 900:
                pet_sound_repeat = now

                out_whine.on() #replace out with other variable
                sleep(0.126)
                out_whine.toggle()
        
         # Run Neopixel "sadLED", green
  
        for i in sadLED['neoNumbers']:
            strip.setPixelColorRGB(i, sadLED['color']['g'], sadLED['color']['r'], sadLED['color']['b'])
            strip.show()
        
        for i in clearLED['neoNumbers']:
            strip.setPixelColorRGB(i, clearLED['color']['g'], clearLED['color']['r'], clearLED['color']['b'])
            strip.show()
            
        return Sad
        
    elif hour >= 23:
    
        # Sound "Grunt"
        pet_sound_repeat = datetime.now()

            now = datetime.now()
            SoundSecs = (now - pet_sound_repeat).total_seconds()

            if SoundSecs > 900:
                pet_sound_repeat = now

                out_grunt.on() #replace out with other variable
                sleep(0.126)
                out_grunt.toggle()
        
         # Run Neopixel "angryLED", green
        
        for i in angryLED['neoNumbers']:
            strip.setPixelColorRGB(i, angryLED['color']['g'], angryLED['color']['r'], angryLED['color']['b'])
            strip.show()
            
        for i in clearLED['neoNumbers']:
            strip.setPixelColorRGB(i, clearLED['color']['g'], clearLED['color']['r'], clearLED['color']['b'])
            strip.show()
        
        return Angry
        
    else:
        return IDLE_DAYTIME

while True:
    # Reset state ready for button etc. if it's the middle of the day:
    if state == BUTTON_DONE and middleOfDay():
        state = IDLE_DAYTIME

    # Progress into the correct colour state:
    if state != BUTTON_DONE:
        state = stateForTime()

    buttonState = sampleButton()

    if buttonState and state != IDLE_DAYTIME:
        state = BUTTON_DONE

    now = datetime.now()
    deltaSecs = (now - jsonLastWrittenTime).total_seconds()

    if deltaSecs > 15:
        writeJSON()
        jsonLastWrittenTime = now

    time.sleep(0.1)
    
    print state
    
    #flush the surpervisor to show log
    sys.stdout.flush()
