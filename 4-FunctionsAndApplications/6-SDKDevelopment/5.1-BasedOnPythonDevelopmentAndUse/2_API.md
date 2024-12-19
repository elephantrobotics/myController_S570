# API 使用说明

> API (Application Programming Interface), 也称为应用程序编程接口函数，是预定义的函数。使用以下函数接口时，请在开始时输入以下代码导入我们的 API 库，否则将无法成功运行

```python
# 例子
from exoskeleton_api import exoskeleton

obj = exoskeleton(port="COM7")

# 获取左臂数据
l_data = obj.get_data(0)
# 获取右臂数据
r_data = obj.get_data(1)
print(l_data)
print(r_data)

# 设置左臂1关节零点
set_zero(0, 1)
# 设置右臂2关节零点
set_zero(1, 2)
```

#### `get_data(arm)`

- **功能：** 获取左右臂数据
- **参数：** 
  - `arm`：0左臂，1右臂
- **返回值：** 角度参数和手部控制器浮点列表：[ J1, J2, J3,  J4,  J5,  J6,  J7, 按钮1，按钮2，摇杆x, 摇杆y]

#### `set_zero(arm, arm_id)`

- **功能：** 设置零点
- **参数：** 
  - `arm`：0左臂，1右臂
  - `arm_id`：关节id，范围 int 1-7
- **返回值：** 无

**注意**：MyController S570 有着极高的兼容能力，适配大象机器人旗下所有产品，以及所有的6-7轴的通用机械臂。所以针对不同的机械臂，有着不同的API函数，请根据实际使用的机械臂型号进行选择。

### 1.mycobot280系列
[https://docs.elephantrobotics.com/docs/mycobot_280_m5_cn/3-FunctionsAndApplications/6.developmentGuide/python/2_API.html](https://docs.elephantrobotics.com/docs/mycobot_280_m5_cn/3-FunctionsAndApplications/6.developmentGuide/python/2_API.html)

### 2.mycobot320系列
[https://docs.elephantrobotics.com/docs/mycobot_320_m5_cn/10-ApplicationBasePython/10.2_320_M5-ApplicationPython/2_API.html](https://docs.elephantrobotics.com/docs/mycobot_320_m5_cn/10-ApplicationBasePython/10.2_320_M5-ApplicationPython/2_API.html)

### 3.MyAGV系列
[https://docs.elephantrobotics.com/docs/myagv_jn23_cn/6-SDKDevelopment/6.1-ApplicationBasePython/6.1.2-API.html](https://docs.elephantrobotics.com/docs/myagv_jn23_cn/6-SDKDevelopment/6.1-ApplicationBasePython/6.1.2-API.html)

### 4.Mercury系列
[https://docs.elephantrobotics.com/docs/Mercury_X1_cn/6-SDKDevelopment/6.1-Python/6.1.2-ApplicationBasePython.html](https://docs.elephantrobotics.com/docs/Mercury_X1_cn/6-SDKDevelopment/6.1-Python/6.1.2-ApplicationBasePython.html)

### 5.MyArm M750
[https://docs.elephantrobotics.com/docs/myarm-master_750-cn/4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/2_API.html](https://docs.elephantrobotics.com/docs/myarm-master_750-cn/4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/2_API.html)

### 6.MechArm系列
[https://docs.elephantrobotics.com/docs/mecharm-m5-cn/7-ApplicationBasePython/7.2_API_270.html](https://docs.elephantrobotics.com/docs/mecharm-m5-cn/7-ApplicationBasePython/7.2_API_270.html)

### 7.MyBuddy
[https://docs.elephantrobotics.com/docs/mybuddy-cn/7-ApplicationBasePython/7.2_API_mybuddy.html](https://docs.elephantrobotics.com/docs/mybuddy-cn/7-ApplicationBasePython/7.2_API_mybuddy.html)


---

[← 上一页](1_download.md) | [下一页 →](3_example.md)