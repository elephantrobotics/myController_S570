# Remote control robot arm case

### mercury X1(7 axes)

Dual-arm cooperative control

```python
import threading
from pymycobot import Mercury
from exoskeleton_api import exoskeleton

obj = exoskeleton(port="/dev/ttyACM4")
ml = Mercury("/dev/left_arm")
mr = Mercury("/dev/right_arm")

# Set both arms to speed fusion mode
ml.set_movement_type(2)
mr.set_movement_type(2)
# Set the jaw operation mode
ml.set_gripper_mode(0)
mr.set_gripper_mode(0)


#0 left arm, 1 right arm
def control_arm(arm):
    while True:
        if arm == 0:
            arm_data = obj.get_data(0)
            print("l: ", arm_data)
            mc = ml
        elif arm == 1:
            arm_data = obj.get_data(1)
            print("r: ", arm_data)
            mc = mr
        else:
            raise ValueError("error arm")
        # Due to the different configurations of each joint steering, zero point and part of the robot arm of the exoskeleton, the mapping relationship is set here (according to the actual steering and position setting of each joint).
        mercury_list = [
            arm_data[0], -arm_data[1], arm_data[2], -arm_data[3], arm_data[4],
            135 + arm_data[5], arm_data[6]
        ]
        # Press the button to control the opening and closing of the claw
        if arm_data[7] == 0:
            mc.set_gripper_state(1, 100)  
        elif arm_data[8] == 0:
            mc.set_gripper_state(0, 100)
        mc.send_angles(mercury_list, 6)


# Left arm
threading.Thread(target=control_arm, args=(0, )).start()
# Right arm
threading.Thread(target=control_arm, args=(1, )).start()
```


---


[← Previous](2_API.md) | [Next page →](4_tracer_API.md)