# MyController S570 Control X1 program case

Connect the exoskeleton to Mercury via USB and save the following script file.
**Note: Make sure each serial number corresponds to the correct device**
## 1.Python API instructions

API (ApplicationProgrammingInterface), also known as application programming interface function, are predefined functions. When using the following functional interface, please enter the following code at the beginning to import our API library, otherwise it will not run successfully:

#### `get_all_data()`

- **Features:** Get dual-arm data

- **Parameters:** None

- **Return value:** Floating point list of Angle parameters and hand controllers:
  
  [[Left arm J1, J2, J3, J4, J5, J6, J7, atom button, stick button, button 1, button 2, stick x, stick y],

  [Right arm J1, J2, J3, J4, J5, J6, J7, atom button, joystick button, button 1, button 2, joystick x, joystick y]

  

#### `get_arm_data(arm)`

- **Features：** Get one-arm data
- **Parameters：** 
  - `arm`：1 left arm, 2 right arm
- **Return value：** Floating point list of Angle parameters and hand controllers: [J1, J2, J3, J4, J5, J6, J7, atom button, joystick button, button 1, button 2, joystick x, joystick y]



#### `get_joint_data(arm, arm_id)`

- **Features：** Obtain single arm and single joint data
- **Parameters：** 
  - `arm`：1 left arm, 2 right arm
  - `arm_id`：Joint id，Radius int 1-7
- **Return value：** angle (int)



#### `set_zero(arm, arm_id)`

- **Features：** Set the current position to joint zero
- **Parameters：** 
  - `arm`：1 left arm, 2 right arm
  - `arm_id`：Joint id，Radius int 1-7
- **Return value：** None



#### `set_color(arm, red, green, blue)`

- **Features：** Set the atom screen color
- **Parameters：** 
  - `arm`：      1 left arm, 2 right arm
  - `red` ：     Radius int 0-255
  - `green` ： Radius int 0-255
  - `blue`：     Radius int 0-255
- **Return value：** None



## 2.Use example

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



###  2.1 Serial communication

```python
# example
from exoskeleton_api import Exoskeleton

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



###  2.2 socket communication

```python
# example
from exoskeleton_api import ExoskeletonSocket

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



## 3 Remote control robot arm case

###  mercury X1(7-axis)

```bash
# The data processing script file is named exoskeleton_api.py
import socket
import threading
import serial

lock = threading.Lock()


class Exoskeleton:
    def __init__(self, port):
        self.ser = serial.Serial(port=port, baudrate=1000000)

    def _parse_data(self, data):
        parsed_data = []
        for i in range(7):
            data_h = data[0 + i * 4: 2 + i * 4]
            data_l = data[2 + i * 4: 4 + i * 4]
            encode = int(data_h + data_l, 16)
            angle = 0 if encode == 2048 else (180 * (encode - 2048) / 2048 if encode > 2048 else -180 * (2048 - encode) / 2048)
            parsed_data.append(round(angle, 2))

        button = bin(int(data[28: 30], 16))[2:].rjust(4, "0")
        parsed_data.extend([int(button[-4]), int(button[-1]), int(button[-3]), int(button[-2]), int(data[30: 32], 16), int(data[32: 34], 16)])
        return parsed_data

    def _commmon(self, command_array):
        with lock:
            commmon_id = command_array[3]
            self.ser.write(command_array)
            start1 = self.ser.read().hex()
            if start1 != "fe" or self.ser.read().hex() != "fe":
                return None
            data_len = int(self.ser.read().hex(), 16)
            count = self.ser.in_waiting
            if data_len == count:
                data = self.ser.read(count).hex()
                if data[-2:] == "fa" and int(data[0: 2], 6) == commmon_id:
                    return data[2: -2]
        return None

    def get_all_data(self):
        get_all_array = [0xFE, 0xFE, 0x02, 0x01, 0xFA]
        data = self._commmon(get_all_array)
        if data is None:
            return None
        left_data = self._parse_data(data)
        right_data = self._parse_data(data[34:])
        return [left_data, right_data]

    def get_arm_data(self, arm):
        if arm not in [1, 2]:
            raise ValueError("error arm")

        send_array = [0xFE, 0xFE, 0x03, 0x02, arm, 0xFA]
        data = self._commmon(send_array)
        if data is None:
            return None
        return self._parse_data(data)

    def get_joint_data(self, arm, id):
        if arm not in [1, 2] or id < 1 or id > 7:
            raise ValueError("error arm or id")

        send_array = [0xFE, 0xFE, 0x04, 0x03, arm, id, 0xFA]
        data = self._commmon(send_array)
        if data is None:
            return None
        encode = int(data[0: 2] + data[2: 4], 16)
        angle = 0 if encode == 2048 else (180 * (encode - 2048) / 2048 if encode > 2048 else -180 * (2048 - encode) / 2048)
        return round(angle, 2)

    def set_zero(self, arm, id):
        if arm not in [1, 2] or id < 1 or id > 7:
            raise ValueError("error arm or id")

        send_array = [0xFE, 0xFE, 0x04, 0x04, arm, id, 0xFA]
        with lock:
            self.ser.write(bytearray(send_array))

    def set_color(self, arm, red, green, blue):
        if arm not in [1, 2]:
            raise ValueError("error arm")
        send_array = [0xFE, 0xFE, 0x06, 0x05, arm, red, green, blue, 0xFA]
        with lock:
            self.ser.write(bytearray(send_array))


class ExoskeletonSocket:
    def __init__(self, ip='192.168.4.1', port=80):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))

    def _commmon(self, command_array):
        with lock:
            commmon_id = command_array[3]
            self.client.sendall(bytearray(command_array))
            if self.client.recv(1).hex() != "fe" or self.client.recv(1).hex() != "fe":
                return None
            data_len = int(self.client.recv(1).hex(), 16) * 2
            data = self.client.recv(1024).hex()
            if len(data) == data_len and data[-2:] == "fa" and int(data[0: 2], 6) == commmon_id:
                return data[2: -2]
        return None

    def _parse_data(self, data):
        parsed_data = []
        for i in range(7):
            data_h = data[0 + i * 4: 2 + i * 4]
            data_l = data[2 + i * 4: 4 + i * 4]
            encode = int(data_h + data_l, 16)
            angle = 0 if encode == 2048 else (180 * (encode - 2048) / 2048 if encode > 2048 else -180 * (2048 - encode) / 2048)
            parsed_data.append(round(angle, 2))

        button = bin(int(data[28: 30], 16))[2:].rjust(4, "0")
        parsed_data.extend([int(button[-4]), int(button[-1]), int(button[-3]), int(button[-2]), int(data[30: 32], 16), int(data[32: 34], 16)])
        return parsed_data

    def get_all_data(self):
        get_all_array = [0xFE, 0xFE, 0x02, 0x01, 0xFA]
        data = self._commmon(get_all_array)
        if data is None:
            return None
        left_data = self._parse_data(data)
        right_data = self._parse_data(data[34:])
        return [left_data, right_data]

    def get_arm_data(self, arm):
        if arm not in [1, 2]:
            raise ValueError("error arm")

        send_array = [0xFE, 0xFE, 0x03, 0x02, arm, 0xFA]
        data = self._commmon(send_array)
        if data is None:
            return None
        return self._parse_data(data)

    def get_joint_data(self, arm, id):
        if arm not in [1, 2] or id < 1 or id > 7:
            raise ValueError("error arm or id")

        send_array = [0xFE, 0xFE, 0x04, 0x03, arm, id, 0xFA]
        data = self._commmon(send_array)
        if data is None:
            return None
        encode = int(data[0: 2] + data[2: 4], 16)
        angle = 0 if encode == 2048 else (180 * (encode - 2048) / 2048 if encode > 2048 else -180 * (2048 - encode) / 2048)
        return round(angle, 2)

    def set_zero(self, arm, id):
        if arm not in [1, 2] or id < 1 or id > 7:
            raise ValueError("error arm or id")

        send_array = [0xFE, 0xFE, 0x04, 0x04, arm, id, 0xFA]
        with lock:
            self.client.sendall(bytearray(send_array))

    def set_color(self, arm, red, green, blue):
        if arm not in [1, 2]:
            raise ValueError("error arm")
        send_array = [0xFE, 0xFE, 0x06, 0x05, arm, red, green, blue, 0xFA]
        with lock:
            self.client.sendall(bytearray(send_array))
```

```bash
# This is a control file named MercuryControl.py
import threading
from pymycobot import Mercury
from exoskeleton_api import Exoskeleton

obj = Exoskeleton(port="/dev/ttyACM4")
ml = Mercury("/dev/left_arm")
mr = Mercury("/dev/right_arm")

ml.set_vr_mode(1)
mr.set_vr_mode(1)
# 设置双臂为速度融合模式
ml.set_movement_type(2)
mr.set_movement_type(2)
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
        mc.send_angles(mercury_list, 6)


# 左臂
threading.Thread(target=control_arm, args=(1, )).start()
# 右臂
threading.Thread(target=control_arm, args=(2, )).start()
```

#### Note: Keep the two files in the same path

#### After successful operation of the program, Mercury X1 can be controlled with the exoskeleton
<video src="../../resources/7-SuccessfulCases/s570.mp4" controls="controls" width="800" height="500"></video>


---



---