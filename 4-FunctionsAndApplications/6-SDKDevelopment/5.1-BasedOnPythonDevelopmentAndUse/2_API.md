# API 使用说明

> API (Application Programming Interface), 也称为应用程序编程接口函数，是预定义的函数。使用以下函数接口时，请在开始时输入以下代码导入我们的 API 库，否则将无法成功运行

## 安装 python 库

```
pip install pymycobot
```

## 使用示例

1. 串口通信

```python
# 例子
from pymycobot.exoskeleton import Exoskeleton

# 连接串口
obj = Exoskeleton(port="COM5")

# 获取双臂数据
all_data = obj.get_all_data()
print(all_data)

# 获取左臂数据
left_data = obj.get_arm_data(1)
print(left_data)

# 获取右臂数据
right_data = obj.get_arm_data(2)
print(right_data)

# 获取单臂单关节数据
joint_data = obj.get_joint_data(1, 1)
print(joint_data)

# 设置当前位置为右臂J7零点
obj.set_zero(2, 7)

# 设置左臂atom屏幕颜色
obj.set_color(1, 0, 255, 0)

# 获取右臂atom固件版本
obj.get_atom_version(2)

# 获取basic固件版本
obj.get_basic_version()
```

2.无线通信

```python
# 例子
from pymycobot.exoskeleton import ExoskeletonSocket

# 连接串口
obj = ExoskeletonSocket()

# 获取双臂数据
all_data = obj.get_all_data()
print(all_data)

# 获取左臂数据
left_data = obj.get_arm_data(1)
print(left_data)

# 获取右臂数据
right_data = obj.get_arm_data(2)
print(right_data)

# 获取单臂单关节数据
joint_data = obj.get_joint_data(1, 1)
print(joint_data)

# 设置当前位置为右臂J7零点
obj.set_zero(2, 7)

# 设置左臂atom屏幕颜色
obj.set_color(1, 0, 255, 0)

# 获取右臂atom固件版本
obj.get_atom_version(2)

# 获取basic固件版本
obj.get_basic_version()
```

#### `get_all_data()`

- **功能：** 获取双臂数据

- **参数：** 无

- **返回值：** 角度参数和手部控制器、坐标浮点列表：

  ​ [[ 左臂 J1, J2, J3, J4, J5, J6, J7, atom 按钮，摇杆按钮，按钮 1，按钮 2，摇杆 x, 摇杆 y, x, y, z, rx, ry, rz],

  ​ [ 右臂 J1, J2, J3, J4, J5, J6, J7, atom 按钮，摇杆按钮， 按钮 1，按钮 2，摇杆 x, 摇杆 y, x, y, z, rx, ry, rz]]

#### `get_arm_data(arm)`

- **功能：** 获取单臂数据
- **参数：**
  - `arm`：1 左臂，2 右臂
- **返回值：** 角度参数和手部控制器浮点列表：[ J1, J2, J3, J4, J5, J6, J7, atom 按钮，摇杆按钮，按钮 1，按钮 2，摇杆 x, 摇杆 y, x, y, z, rx, ry, rz]

#### `get_joint_data(arm, arm_id)`

- **功能：** 获取单臂单关节数据
- **参数：**
  - `arm`：1 左臂，2 右臂
  - `arm_id`：关节 id，范围 int 1-7
- **返回值：** angle (int)

#### `get_joint_data(arm, arm_id)`

- **功能：** 获取单臂单关节数据
- **参数：**
  - `arm`：1 左臂，2 右臂
  - `arm_id`：关节 id，范围 int 1-7
- **返回值：** angle (int)

#### `set_zero(arm, arm_id)`

- **功能：** 将当前位置设置为关节零位
- **参数：**
  - `arm`：1 左臂，2 右臂
  - `arm_id`：关节 id，范围 int 1-7
- **返回值：** 1

#### `set_color(arm, red, green, blue)`

- **功能：** 设置 atom 屏幕颜色
- **参数：**
  - `arm`： 1 左臂，2 右臂
  - `red` ： 范围 int 0-255
  - `green` ： 范围 int 0-255
  - `blue`： 范围 int 0-255
- **返回值：** 1

#### `get_basic_version()`

- **功能：** 获取主控 basic 固件版本号
- **返回值：** 版本号

#### `get_atom_version(arm)`

- **功能：** 获取末端 atom 固件版本号
- **参数：**
  - `arm`： 1 左臂，2 右臂
- **返回值：** 版本号

**注意**：MyController S570 有着极高的兼容能力，适配大象机器人旗下所有产品，以及所有的 6-7 轴的通用机械臂。所以针对不同的机械臂，有着不同的 API 函数，请根据实际使用的机械臂型号进行选择。

### 1.mycobot280 系列

[https://docs.elephantrobotics.com/docs/mycobot_280_m5_cn/3-FunctionsAndApplications/6.developmentGuide/python/2_API.html](https://docs.elephantrobotics.com/docs/mycobot_280_m5_cn/3-FunctionsAndApplications/6.developmentGuide/python/2_API.html)

### 2.mycobot320 系列

[https://docs.elephantrobotics.com/docs/mycobot_320_m5_cn/10-ApplicationBasePython/10.2_320_M5-ApplicationPython/2_API.html](https://docs.elephantrobotics.com/docs/mycobot_320_m5_cn/10-ApplicationBasePython/10.2_320_M5-ApplicationPython/2_API.html)

### 3.MyAGV 系列

[https://docs.elephantrobotics.com/docs/myagv_jn23_cn/6-SDKDevelopment/6.1-ApplicationBasePython/6.1.2-API.html](https://docs.elephantrobotics.com/docs/myagv_jn23_cn/6-SDKDevelopment/6.1-ApplicationBasePython/6.1.2-API.html)

### 4.Mercury 系列

[https://docs.elephantrobotics.com/docs/Mercury_X1_cn/6-SDKDevelopment/6.1-Python/6.1.2-ApplicationBasePython.html](https://docs.elephantrobotics.com/docs/Mercury_X1_cn/6-SDKDevelopment/6.1-Python/6.1.2-ApplicationBasePython.html)

### 5.MyArm M750

[https://docs.elephantrobotics.com/docs/myarm-master_750-cn/4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/2_API.html](https://docs.elephantrobotics.com/docs/myarm-master_750-cn/4-FunctionsAndApplications/6-SDKDevelopment/5.1-BasedOnPythonDevelopmentAndUse/2_API.html)

### 6.MechArm 系列

[https://docs.elephantrobotics.com/docs/mecharm-m5-cn/7-ApplicationBasePython/7.2_API_270.html](https://docs.elephantrobotics.com/docs/mecharm-m5-cn/7-ApplicationBasePython/7.2_API_270.html)

### 7.MyBuddy

[https://docs.elephantrobotics.com/docs/mybuddy-cn/7-ApplicationBasePython/7.2_API_mybuddy.html](https://docs.elephantrobotics.com/docs/mybuddy-cn/7-ApplicationBasePython/7.2_API_mybuddy.html)

---

[← 上一页](1_download.md) | [下一页 →](3_example.md)
