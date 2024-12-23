# API instructions

Application Programming Interface (API), also known as application Programming interface functions, is a predefined function. When using the following function interface, please import our API library by entering the following code at the beginning, otherwise it will not run successfully

```python
# Examples
from exoskeleton_api import exoskeleton

obj = exoskeleton(port="COM7")

# Get left arm data
l_data = obj.get_data(0)
# Get right arm data
r_data = obj.get_data(1)
print(l_data)
print(r_data)

# Set left arm 1 joint zero
set_zero(0, 1)
# Set the zero point of the right arm 2 joints
set_zero(1, 2)
```

#### `get_data(arm)`

- ** Function: ** Get left and right arm data
- ** Parameter: **
- 'arm' : 0 left arm, 1 right arm
- ** Return value: ** Angle parameters and hand controller floating point list: [J1, J2, J3, J4, J5, J6, J7, button 1, button 2, joystick x, joystick y]

#### `set_zero(arm, arm_id)`

- ** Function: ** Set zero
- ** Parameter: **
- 'arm' : 0 left arm, 1 right arm
- 'arm_id' : specifies the id of the joint. The value ranges from int 1 to 7
- ** Returned value: ** None

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