from gpiozero import OutputDevice
from time import sleep
from datetime import datetime


pet_sound_repeat = datetime.now()

out= OutputDevice(6,False)

while True:

    now = datetime.now()
    SoundSecs = (now - pet_sound_repeat).total_seconds()

    if SoundSecs > 4:
        pet_sound_repeat = now

        out.on()
        sleep(0.126)
        out.toggle()

