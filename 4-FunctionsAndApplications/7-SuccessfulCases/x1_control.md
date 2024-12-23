# MyController S570 Control X1 program case

Connect the exoskeleton to Mercury via USB and save the following script file.
**Note: Make sure each serial number corresponds to the correct device**

```bash
# The data processing script file is named exoskeleton_api.py
import threading
import time
import serial

lock = threading.Lock()


data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
set_zero_data = [0xA5, 0x01, 0x00, 0x02, 0x5A]
# The command represents the left and right arms
hex_array_l = bytearray([0xA5, 0x01, 0x00, 0x06, 0x5A])  # Left arm
hex_array_r = bytearray([0xA5, 0x01, 0x00, 0x07, 0x5A])  # Right arm


class exoskeleton:

    def __init__(self, port):
        self.ser = serial.Serial(port=port, baudrate=1000000)

    # 0: Left arm
    # 1: Right arm
    def get_data(self, arm):
        with lock:
            if arm == 0:
                self.ser.write(hex_array_l)
            elif arm == 1:
                self.ser.write(hex_array_r)
            else:
                raise ValueError("error arm")
            time.sleep(0.01)
            count = self.ser.in_waiting
            data = self.ser.read(count).hex()
            print(data)
            if len(data) == 84 and data[0:2] == "d5" and data[-2:] == "5d":
                for i in range(7):
                    data_h = data[8 + i * 10: 10 + i * 10]
                    data_l = data[10 + i * 10: 12 + i * 10]
                    encode = int(data_h + data_l, 16)
                    if encode == 2048:
                        angle = 0
                    elif encode < 2048:
                        angle = -180 * (2048 - encode) / 2048
                    else:
                        angle = 180 * (encode - 2048) / 2048
                    data_list[i] = round(angle, 2)
                button = bin(int(data[-10: -8]))[2:].rjust(4, "0")
                data_list[7] = int(button[1])
                data_list[8] = int(button[2])
                data_list[9] = int(data[-6: -4], 16)
                data_list[10] = int(data[-4: -2], 16)
                return data_list
            else:
                return None

    # 0: Left arm
    # 1: Right arm
    def set_zero(self, arm, arm_id):
        with lock:
            if arm == 0:
                set_zero_data[3] = 0x12
            elif arm == 1:
                set_zero_data[3] = 0x02
            else:
                raise ValueError("error arm")
            if 1 <= arm_id <= 7:
                set_zero_data[1] = arm_id
            else:
                raise ValueError("error id")
            self.ser.write(bytearray(set_zero_data))
```
```bash
# Control script file
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


# 0 left arm, 1 right arm
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
        mercury_list = [
            arm_data[0], -arm_data[1], arm_data[2], -arm_data[3], arm_data[4],
            135 + arm_data[5], arm_data[6]
        ]
        if arm_data[7] == 0:
            mc.set_gripper_state(1, 100)
        elif arm_data[8] == 0:
            mc.set_gripper_state(0, 100)
        # mc.send_angles(mercury_list, 6)


# Left arm
threading.Thread(target=control_arm, args=(0, )).start()
# Right arm
threading.Thread(target=control_arm, args=(1, )).start()
```

#### Note: Keep the two files in the same path

#### After successful operation of the program, Mercury X1 can be controlled with the exoskeleton
<video src="../../resources/7-SuccessfulCases/s570.mp4" controls="controls" width="800" height="500"></video>


---



---