# Simple example of running periodic tasks in a script with a 0.1 second strobe.

from datetime import datetime
import time
import demo_SOUND
#import demo_LED


# For each task, a predefined interval:

TASK_A_INTERVAL = 1.5
TASK_B_INTERVAL = 2.9
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
        demo_SOUND.hello()
        demo_LED.mode_smile()

def task_B():
    global task_B_last_done

    now = datetime.now()
    deltaSecs = (now - task_B_last_done).total_seconds()

    if deltaSecs > TASK_B_INTERVAL:
        print("[  B  ]")
        demo_SOUND.neutral()
        
        task_B_last_done = now

def task_C():
    global task_C_last_done

    now = datetime.now()
    deltaSecs = (now - task_C_last_done).total_seconds()

    if deltaSecs > TASK_C_INTERVAL:
        print("[    C]")
        task_C_last_done = now
        demo_SOUND.sad()

# Main loop. Only one loop needed in the whole script: the tasks are polled to
# see if they want to do anything. This loop runs 10 times a second, though the
# tasks fire much less frequently than that.

while True:
    task_A()
    task_B()
    task_C()
    time.sleep(0.1)
