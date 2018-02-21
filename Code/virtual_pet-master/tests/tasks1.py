# Simple example of running periodic tasks in a script with a 0.1 second strobe.

from datetime import datetime
import time
import demo_SOUND
import demo_MODE
import demo_LED
import demo_BUTTON

pressed = False

# For each task, a predefined interval:

TASK_A_INTERVAL = 3
TASK_B_INTERVAL = 0.1
TASK_C_INTERVAL = 10

# For each task, track when it last fired:

task_A_last_done = datetime.now()
task_B_last_done = datetime.now()
task_C_last_done = datetime.now()



def task_A():
    # A Python thing: declare these variables as "global" since otherwise an assignment
    # to them will create a new local of the same name, probably not what's intended.
    global task_A_last_done

    now = datetime.now()
    deltaSecs = (now - task_A_last_done).total_seconds()

    if deltaSecs > TASK_A_INTERVAL:
        print("[A    ]")
        task_A_last_done = now
        if pressed:
            demo_MODE.modeReset()
        m = demo_MODE.changeMode()
        demo_SOUND.sound(m)
        demo_LED.LED(m)
        

def task_B():

    global task_B_last_done
    global pressed
    global task_A_last_done

    now = datetime.now()
    deltaSecs = (now - task_B_last_done).total_seconds()

    if deltaSecs > TASK_B_INTERVAL:
        print("[  B   ]")
        task_B_last_done = now
        pressed = demo_BUTTON.press()
        
        if pressed:
            task_A_last_done = datetime(1970,1,1)
        
        

# Main loop. Only one loop needed in the whole script: the tasks are polled to
# see if they want to do anything. This loop runs 10 times a second, though the
# tasks fire much less frequently than that.

while True:
    task_A()
    task_B()
    #task_C()
    time.sleep(0.1)
