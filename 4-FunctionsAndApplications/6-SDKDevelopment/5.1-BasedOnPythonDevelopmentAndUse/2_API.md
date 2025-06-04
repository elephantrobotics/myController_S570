# API instructions

Application Programming Interface (API), also known as application Programming interface functions, is a predefined function. When using the following function interface, please import our API library by entering the following code at the beginning, otherwise it will not run successfully

Install the python library

` ` `https://github.com/elephantrobotics/pymycobot.git` ` `

## Usage Example

1.Serial communication

## Example Usage

1. Serial Communication

```python
# Example
from pymycobot import Exoskeleton

# Connect to serial port
obj = Exoskeleton(port="COM5")

# Get data from both arms
all_data = obj.get_all_data()
print(all_data)

# Get left arm data
left_data = obj.get_arm_data(1)
print(left_data)

# Get right arm data
right_data = obj.get_arm_data(2)
print(right_data)

# Get data of a single joint on one arm
joint_data = obj.get_joint_data(1, 1)
print(joint_data)

# Set current position of right arm J7 as zero
obj.set_zero(2, 7)

# Set color of left arm atom screen
obj.set_color(1, 0, 255, 0)

# Get firmware version of right arm atom
obj.get_atom_version(2)

# Get basic firmware version
obj.get_basic_version()
```

2.Wireless Communication

```python
# Example
from pymycobot import ExoskeletonSocket

# Connect to socket
obj = ExoskeletonSocket()

# Get data from both arms
all_data = obj.get_all_data()
print(all_data)

# Get left arm data
left_data = obj.get_arm_data(1)
print(left_data)

# Get right arm data
right_data = obj.get_arm_data(2)
print(right_data)

# Get data of a single joint on one arm
joint_data = obj.get_joint_data(1, 1)
print(joint_data)

# Set current position of right arm J7 as zero
obj.set_zero(2, 7)

# Set color of left arm atom screen
obj.set_color(1, 0, 255, 0)

# Get firmware version of right arm atom
obj.get_atom_version(2)

# Get basic firmware version
obj.get_basic_version()
```

#### `get_all_data()`

- ** Function ** : Obtain data from both arms

- ** Parameters: ** None

- ** Return value ** : Angle parameter and hand controller, coordinate floating-point list:

[[Left arm J1, J2, J3, J4, J5, J6, J7, atom button, joystick button, Button 1, Button 2, joystick x, joystick y, x, y, z, rx, ry, rz]

[Right arm J1, J2, J3, J4, J5, J6, J7, atom button, joystick button, Button 1, Button 2, joystick x, joystick y, x, y, z, rx, ry, rz]]

#### `get_arm_data(arm)`

- ** Function ** : Obtain single-arm data
- ** Parameter **
- 'arm' : 1 left arm, 2 right arm
- ** Return Value ** Angle parameters and hand controller floating-point list: [J1, J2, J3, J4, J5, J6, J7, atom button, joystick button, Button 1, Button 2, joystick x, joystick y, x, y, z, rx, ry, rz]

#### `get_joint_data(arm, arm_id)`

- ** Function ** : Obtain data of a single arm and a single joint
- ** Parameter **
- 'arm' : 1 left arm, 2 right arm
- 'arm_id' : Joint id, range int 1-7
- ** Return value: ** angle (int)

#### `get_joint_data(arm, arm_id)`

- ** Function ** : Obtain data of a single arm and a single joint
- ** Parameter **
- 'arm' : 1 left arm, 2 right arm
- 'arm_id' : Joint id, range int 1-7
- ** Return value: ** angle (int)

#### `set_zero(arm, arm_id)`

- ** Function ** : Set the current position to the zero position of the joint
- ** Parameter **
- 'arm' : 1 left arm, 2 right arm
- 'arm_id' : Joint id, range int 1-7
- ** Return value ** 1

#### `set_color(arm, red, green, blue)`

- ** Function ** : Set the color of the atom screen
- ** Parameter **
- 'arm' : 1 left arm, 2 right arm
- 'red' : Range int 0-255
- 'green' : Range int 0-255
- 'blue' : Range int 0-255
- ** Return value ** 1

#### `get_basic_version()`

- ** Function ** : Obtain the version number of the main control basic firmware
- ** Return value: ** Version number

#### `get_atom_version(arm)`

- ** Function ** : Obtain the terminal atom firmware version number
- ** Parameter **
- 'arm' : 1 left arm, 2 right arm
- ** Return value: ** Version number

**Note** : MyController S570 is extremely compatible with all Elephant Robot products, as well as all general purpose 6-7 axis robot arms. Therefore, for different robot arms, there are different API functions, please choose according to the actual model of the robot arm.

### 1.mycobot280series

[https://docs.elephantrobotics.com/docs/mycobot_280_m5_cn/3-FunctionsAndApplications/6.developmentGuide/python/2_API.html](https://docs.elephantrobotics.com/docs/mycobot_280_m5_cn/3-FunctionsAndApplications/6.developmentGuide/python/2_API.html)

### 2.mycobot320series

[https://docs.elephantrobotics.com/docs/mycobot_320_m5_cn/10-ApplicationBasePython/10.2_320_M5-ApplicationPython/2_API.html](https://docs.elephantrobotics.com/docs/mycobot_320_m5_cn/10-ApplicationBasePython/10.2_320_M5-ApplicationPython/2_API.html)

### 3.MyAGVseries

[https://docs.elephantrobotics.com/docs/myagv_jn23_cn/6-SDKDevelopment/6.1-ApplicationBasePython/6.1.2-API.html](https://docs.elephantrobotics.com/docs/myagv_jn23_cn/6-SDKDevelopment/6.1-ApplicationBasePython/6.1.2-API.html)

### 4.Mercuryseries

[https://docs.elephantrobotics.com/docs/Mercury_X1_cn/6-SDKDevelopment/6.1-Python/6.1.2-ApplicationBasePython.html](https://docs.elephantrobotics.com/docs/Mercury_X1_cn/6-SDKDevelopment/6.1-Python/6.1.2-ApplicationBasePython.html)

### 5.MyArm M750

[https://docs.elephantrobotics.com/docs/myarm-master_750-cn/4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/2_API.html](https://docs.elephantrobotics.com/docs/myarm-master_750-cn/4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/2_API.html)

### 6.MechArmseries

[https://docs.elephantrobotics.com/docs/mecharm-m5-cn/7-ApplicationBasePython/7.2_API_270.html](https://docs.elephantrobotics.com/docs/mecharm-m5-cn/7-ApplicationBasePython/7.2_API_270.html)

### 7.MyBuddy

[https://docs.elephantrobotics.com/docs/mybuddy-cn/7-ApplicationBasePython/7.2_API_mybuddy.html](https://docs.elephantrobotics.com/docs/mybuddy-cn/7-ApplicationBasePython/7.2_API_mybuddy.html)

---

[← Previous](1_download.md) | [Next page →](3_example.md)

```

```
