# MyController S570 Control AGV+280M5 program case
Connect the exoskeleton to the Jetson Nano system on the AGV via USB and save and run the following script file.
> **Note: Make sure each serial number corresponds to the correct device**
>
> **Recommended to start this case: atom version 6.5; The pymycobot version 3.6.8**

```bash
import threading
import time

import serial
from pymycobot import *
from exoskeleton_api import exoskeleton
from mercury_ros_api import MapNavigation
from pymycobot.mycobot import MyCobot
from pymycobot.utils import get_port_list


mr = MyCobot("/dev/ttyACM3",115200)

obj = exoskeleton(port="/dev/ttyACM4")


map_navigation = MapNavigation()
mr.power_on()


def Pump_testing_open():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)

    # open
    GPIO.output(3, GPIO.LOW)
    GPIO.output(2, GPIO.HIGH)


def Pump_testing_close():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    # close
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(2, GPIO.HIGH)


def move(x, y):
    if y < 50:
        map_navigation.pub_vel(0.25, 0, 0)
    elif y > 200:
        map_navigation.pub_vel(-0.25, 0, 0)
    elif x < 50:
        map_navigation.pub_vel(0, 0, -0.5)
    elif x > 200:
        map_navigation.pub_vel(0, 0, 0.5)
    else:
        map_navigation.pub_vel(0, 0, 0)
        #map_navigation.stop()


# 0 left arm, 1 right arm
def control_arm(arm):
    while True:
        if arm == 0:
            arm_data = obj.get_data(0)
            x, y = arm_data[9], arm_data[10]
            print("l: ", arm_data)
            # mc = ml
            mc = mr
        elif arm == 1:
            arm_data = obj.get_data(1)
            x, y = arm_data[9], arm_data[10]
            print("r: ", arm_data)
            mc = mr
            threading.Thread(target=move, args=(x, y,)).start()
        else:
            raise ValueError("error arm")
        mercury_list = [
            -arm_data[1]-40, arm_data[0] - 90, -arm_data[3], arm_data[5],
            arm_data[4], arm_data[6]
        ]
        #mercury_list = [
        #    0, 0, 0, 0, 0,
        #    arm_data[6]
        #]
        if arm_data[7] == 0:
            Pump_testing_open()
        elif arm_data[8] == 0:
            Pump_testing_close()
        mc.send_angles(mercury_list, 100)

# The right arm of the exoskeleton controls AGV+280M5
threading.Thread(target=control_arm, args=(1, )).start()


```

### The AGV+280M5 can be controlled with the exoskeleton after the program has been successfully run
<video src="../../resources/7-SuccessfulCases/s570.mp4" controls="controls" width="800" height="500"></video>


---



---