# MyController S570 Control X1 program case

Connect the exoskeleton to Mercury via USB and save the following script file.
**Note: Make sure each serial number corresponds to the correct device**

## 1.Use example

Operation tutorial:

Turn on the side switch before inserting Type-C

<img src="../../resources/7-SuccessfulCases/1.jpg" alt="7.1.1-1" style="zoom:100%;" />

Turn on wifi:

Press button A, IP is displayed for use, wifi account number: elephant, wifi password elephant

Turn off wifi: press button C

Turn on Bluetooth:

Press button B, display BT can be used, Bluetooth name BLE

Turn off Bluetooth: press button C

<img src="../../resources/7-SuccessfulCases/2.jpg" alt="7.1.1-1" style="zoom:100%;" />

### 1.1 Serial communication

```python
# example
from pymycobot import Exoskeleton

# Connect the serial port
obj = Exoskeleton(port="COM5")

# Get dual-arm data
all_data = obj.get_all_data()
print(all_data)

# Get left arm data
left_data = obj.get_arm_data(1)
print(left_data)

# Get right arm data
right_data = obj.get_arm_data(2)
print(right_data)

# Obtain single arm and single joint data
joint_data = obj.get_joint_data(1, 1)
print(joint_data)

# Set the current position to zero on right arm J7
obj.set_zero(2, 7)

# Set the left arm atom screen color
obj.set_color(1, 0, 255, 0)
```

### 1.2 socket communication

```python
# example
from pymycobot import ExoskeletonSocket

# Connection server
obj = ExoskeletonSocket()

# Get dual-arm data
all_data = obj.get_all_data()
print(all_data)

# Get left arm data
left_data = obj.get_arm_data(1)
print(left_data)

# Get right arm data
right_data = obj.get_arm_data(2)
print(right_data)

# Obtain single arm and single joint data
joint_data = obj.get_joint_data(1, 1)
print(joint_data)

# Set the current position to zero on right arm J7
obj.set_zero(2, 7)

# Set the left arm atom screen color
obj.set_color(1, 0, 255, 0)
```

## 2 Remote control robot arm case

### mercury X1(7-axis)  

```bash
# The version of pymycobot should be 4.0.0 or above
# This is a control file named MercuryControl.py
import threading
from pymycobot import Mercury
from pymycobot import Exoskeleton

obj = Exoskeleton(port="/dev/ttyACM4")
ml = Mercury("/dev/left_arm")
mr = Mercury("/dev/right_arm")

ml.set_vr_mode(1)
mr.set_vr_mode(1)
# 设置双臂为速度融合模式
ml.set_movement_type(3)
mr.set_movement_type(3)
# 设置夹爪运行模式
ml.set_gripper_mode(0)
mr.set_gripper_mode(0)


# 1 左臂，2 右臂
def control_arm(arm):
    while True:
        if arm == 1:
            arm_data = obj.get_arm_data(1)
            print("l: ", arm_data)
            mc = ml
        elif arm == 2:
            arm_data = obj.get_arm_data(2)
            print("r: ", arm_data)
            mc = mr
        else:
            raise ValueError("error arm")
        # 由于外骨骼各关节转向、零点与部分机械臂构型不同，在此设置映射关系(根据各关节实际控制转向、位置设置)
        mercury_list = [
            arm_data[0], -arm_data[1], arm_data[2], -arm_data[3], arm_data[4],
            135 + arm_data[5], arm_data[6]
        ]
        if arm_data[9] == 0:
            mc.set_gripper_state(1, 100)
        elif arm_data[10] == 0:
            mc.set_gripper_state(0, 100)
        mc.send_angles(mercury_list, 6, _async=True)


# 左臂
threading.Thread(target=control_arm, args=(1, )).start()
# 右臂
threading.Thread(target=control_arm, args=(2, )).start()
```

#### Note: Keep the two files in the same path

#### After successful operation of the program, Mercury X1 can be controlled with the exoskeleton

<video src="../../resources/7-SuccessfulCases/s570.mp4" controls="controls" width="800" height="500"></video>

## Exoskeleton control Mercury X1 specific case

### Case 1: Exoskeleton controls Mercury X1+ three-finger dexterous hand to drill holes with electric drill

Source code

```python
# This is a control file named MercuryControl.py
import threading
from pymycobot import Mercury
import time
from pymycobot import Exoskeleton
import os

os.system("sudo chmod 777 /dev/ttyACM*")

obj = Exoskeleton(port="/dev/ttyACM4")

ml = Mercury("/dev/left_arm")
mr = Mercury("/dev/right_arm")

l_control_mode = 1
r_control_mode = 1

l_last_mode = 0
r_last_mode = 0

ml.set_movement_type(3)
mr.set_movement_type(3)

ml.set_vr_mode(1)
mr.set_vr_mode(1)

ml.set_hand_gripper_angle(14, 4, 90)
ml.set_hand_gripper_angle(14, 5, 20)
ml.set_hand_gripper_angle(14, 6, 30)
ml.set_hand_gripper_angle(14, 1, 50)
ml.set_hand_gripper_angle(14, 3, 90)


def jointlimit(angles):
    max = [165, 120, 175, 0, 175, 180, 175]
    min = [-165, -50, -175, -175, -175, 60, -175]
    for i in range(7):
        if angles[i] > max[i]:
            angles[i] = max[i]
        if angles[i] < min[i]:
            angles[i] = min[i]


def gripper_control_open_2(mc):
    mc.set_hand_gripper_angle(14, 2, 0)


def gripper_control_close_2(mc):
    mc.set_hand_gripper_angle(14, 2, 90)


# 1 left，2 right
def control_arm(arm):
    global l_control_mode, l_last_mode, r_control_mode, r_last_mode
    st = 0
    while True:
        try:
            if arm == 1:
                arm_data = obj.get_arm_data(1)
                print("l: ", arm_data)
                mc = ml
            elif arm == 2:
                arm_data = obj.get_arm_data(2)
                print("r: ", arm_data)
                mc = mr
            else:
                raise ValueError("error arm")
            time_err = 1000 * (time.time() - st)
            st = time.time()
            if arm == 1:
                mercury_list = [
                    arm_data[0] - 10, -arm_data[1], arm_data[2], -arm_data[3], 105, 38, 0
                ]
                jointlimit(mercury_list)
                if arm_data[7] == 0 and l_last_mode == 0:
                    print(6)
                    l_last_mode = 1
                    l_control_mode += 1
                    if l_control_mode > 3:
                        l_control_mode = 1

                    if l_control_mode == 1:
                        obj.set_color(arm, 0, 255, 0)
                    elif l_control_mode == 2:
                        obj.set_color(arm, 0, 0, 255)
                    else:
                        obj.set_color(arm, 255, 0, 0)

                if arm_data[7] == 1:
                    l_last_mode = 0

                if l_control_mode == 1:
                    TI = 10
                elif l_control_mode == 2:
                    TI = 5
                else:
                    TI = 3
                if arm_data[9] == 0:
                    threading.Thread(target=gripper_control_close_2, args=(mc,)).start()

                elif arm_data[10] == 0:
                    threading.Thread(target=gripper_control_open_2, args=(mc,)).start()
                if arm_data[9] == 0 and arm_data[10] == 0:
                    time.sleep(0.01)
                    continue

            else:
                mercury_list = [
                    arm_data[0], -arm_data[1], -0.524, -41.862, -90.686, 101.273, 25.257
                ]
                jointlimit(mercury_list)
                if arm_data[7] == 0 and r_last_mode == 0:
                    print(6)
                    r_last_mode = 1
                    r_control_mode += 1
                    if r_control_mode > 3:
                        r_control_mode = 1
                    if r_control_mode == 1:
                        obj.set_color(arm, 0, 255, 0)
                    elif r_control_mode == 2:
                        obj.set_color(arm, 0, 0, 255)
                    else:
                        obj.set_color(arm, 255, 0, 0)

                if arm_data[7] == 1:
                    r_last_mode = 0
                if r_control_mode == 1:
                    TI = 10
                elif r_control_mode == 2:
                    TI = 5
                else:
                    TI = 3

            mc.send_angles(mercury_list, TI, _async=True)
            time.sleep(0.01)

        except Exception as e:
            print(e)
            pass


threading.Thread(target=control_arm, args=(1,)).start()
threading.Thread(target=control_arm, args=(2,)).start()
```

Case video
<video src="../../resources/7-SuccessfulCases/0214.mp4" controls="controls" width="800" height="500"></video>

### Case 2: Exoskeleton control Mercury X1+ force control claw

Source code

```python
import threading
from pymycobot import Mercury
import time
from exoskeleton_api import Exoskeleton, ExoskeletonSocket
import os

os.system("sudo chmod 777 /dev/ttyACM*")

obj = Exoskeleton(port="/dev/ttyACM4")

ml = Mercury("/dev/left_arm")
mr = Mercury("/dev/right_arm")

l_control_mode = 1
r_control_mode = 1

l_last_mode = 0
r_last_mode = 0

ml.set_movement_type(3)
mr.set_movement_type(3)

ml.set_vr_mode(1)
mr.set_vr_mode(1)


def jointlimit(angles):
    max = [165, 120, 175, 0, 175, 180, 175]
    min = [-165, -50, -175, -175, -175, 60, -175]
    for i in range(7):
        if angles[i] > max[i]:
            angles[i] = max[i]
        if angles[i] < min[i]:
            angles[i] = min[i]


def gripper_control_open(mc):
    mc.set_pro_gripper_angle(14, 80)


def gripper_control_close(mc):
    mc.set_pro_gripper_angle(14, 0)


def control_arm(arm):
    global l_control_mode, l_last_mode, r_control_mode, r_last_mode
    st = 0
    while True:
        try:
            if arm == 1:
                arm_data = obj.get_arm_data(1)
                print("l: ", arm_data)
                mc = ml
            elif arm == 2:
                arm_data = obj.get_arm_data(2)
                print("r: ", arm_data)
                mc = mr
            else:
                raise ValueError("error arm")
            mercury_list = [
                arm_data[0], -arm_data[1], arm_data[2], -arm_data[3], arm_data[4],
                135 + arm_data[5], arm_data[6] - 30
            ]
            jointlimit(mercury_list)
            time_err = 1000 * (time.time() - st)
            st = time.time()
            if arm == 1:
                if arm_data[7] == 0 and l_last_mode == 0:
                    print(6)
                    l_last_mode = 1
                    l_control_mode += 1
                    if l_control_mode > 3:
                        l_control_mode = 1

                    if l_control_mode == 1:
                        obj.set_color(arm, 0, 255, 0)
                    elif l_control_mode == 2:
                        obj.set_color(arm, 0, 0, 255)
                    else:
                        obj.set_color(arm, 255, 0, 0)

                if arm_data[7] == 1:
                    l_last_mode = 0

                if l_control_mode == 1:
                    TI = 10
                elif l_control_mode == 2:
                    TI = 5
                else:
                    TI = 3
            else:
                if arm_data[7] == 0 and r_last_mode == 0:
                    print(6)
                    r_last_mode = 1
                    r_control_mode += 1
                    if r_control_mode > 3:
                        r_control_mode = 1
                    if r_control_mode == 1:
                        obj.set_color(arm, 0, 255, 0)
                    elif r_control_mode == 2:
                        obj.set_color(arm, 0, 0, 255)
                    else:
                        obj.set_color(arm, 255, 0, 0)

                if arm_data[7] == 1:
                    r_last_mode = 0
                if r_control_mode == 1:
                    TI = 10
                elif r_control_mode == 2:
                    TI = 5
                else:
                    TI = 3

            if arm_data[9] == 0:
                threading.Thread(target=gripper_control_close, args=(mc,)).start()

            elif arm_data[10] == 0:
                threading.Thread(target=gripper_control_open, args=(mc,)).start()

            if arm_data[9] == 0 and arm_data[10] == 0:
                time.sleep(0.01)
                    continue

            mc.send_angles(mercury_list, TI, _async=True)
            time.sleep(0.01)

        except Exception as e:
            print(e)
            pass

threading.Thread(target=control_arm, args=(1,)).start()
threading.Thread(target=control_arm, args=(2,)).start()
```

---

---
