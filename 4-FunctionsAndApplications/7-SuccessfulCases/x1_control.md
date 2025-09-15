# MyController S570 控制 X1 程序案例

### 将外骨骼通过 USB 的方式连接上水星上，并保存以下脚本文件。

**注意：确保每个串口号对应的设备是正确的**

## 1.使用示例

操作教程：

先打开侧边开关再插入 Type-C

<img src="../../resources/7-SuccessfulCases/1.jpg" alt="7.1.1-1" style="zoom:100%;" />

打开 wifi:

按下按键 A，显示 IP 即可使用，wifi 账号：elephant，wifi 密码 elephant

关闭 wifi：按下按键 C

打开蓝牙:

按下按键 B，显示 BT 即可使用，蓝牙名称 BLE

关闭蓝牙：按下按键 C

<img src="../../resources/7-SuccessfulCases/2.jpg" alt="7.1.1-1" style="zoom:100%;" />

### 1.1 串口通信

```python
# 例子
from pymycobot import Exoskeleton

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
```

### 1.2 socket 通信

```python
# 例子
from pymycobot import ExoskeletonSocket

# 连接服务端
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
```

## 2.遥操控制机械臂案例

### mercury X1(7 轴)

双臂协同控制 pymycobot 库版本：4.0.0及以上版本

```bash
# 本文件为控制文件，命名为：MercuryControl.py
import threading
from pymycobot import Mercury
from pymycobot import Exoskeleton

obj = Exoskeleton(port="/dev/ttyACM4") #根据外骨骼串口号更改
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

#### 注意：要将这两个文件放在同一路径下

### 程序成功运行之后即可用外骨骼控制水星 X1

<video src="../../resources/7-SuccessfulCases/s570.mp4" controls="controls" width="800" height="500"></video>

## 外骨骼控制水星 X1 具体案例

### 案例一：外骨骼控制水星 X1+三指灵巧手进行电钻打孔

源码

```python
# 本文件为控制文件，命名为：MercuryControl.py
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

# 设置双臂为速度融合模式
ml.set_movement_type(3)
mr.set_movement_type(3)
# 设置VR模式
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


# 1 左臂，2 右臂
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

            else:  # 右臂
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


# 左臂
threading.Thread(target=control_arm, args=(1,)).start()
# 右臂
threading.Thread(target=control_arm, args=(2,)).start()

```

案例视频
<video src="../../resources/7-SuccessfulCases/0214.mp4" controls="controls" width="800" height="500"></video>

### 案例二：外骨骼控制水星 X1+力控夹爪+摇杆控制水星移动
#### 注意：当水星的电压低于21v时，则无法控制移动；使用前请检查外骨骼与水星双臂的映射关系是否正确

源码

```python
import os
import threading
import time
import serial
from pymycobot import *
from pymycobot.utils import get_port_list

os.system("sudo chmod 777 /dev/ttyACM*")
move = ChassisControl(port="/dev/wheeltec_controller")
obj = Exoskeleton(port="/dev/ttyACM4")
ml = Mercury("/dev/left_arm")
mr = Mercury("/dev/right_arm")

# 设置模式
ml.set_movement_type(3)
mr.set_movement_type(3)
ml.set_vr_mode(1)
mr.set_vr_mode(1)
ml.set_pro_gripper_speed(14, 100)
mr.set_pro_gripper_speed(14, 100)

# 定义全局状态变量
last_move_cmd = None
last_rotation_cmd = None
move_lock = threading.Lock()


# 控制力控夹爪开闭
def control_gripper(mc, mode):
    if mode == 1:
        mc.set_pro_gripper_angle(14, 100)
    elif mode == 2:
        mc.set_pro_gripper_angle(14, 10)
    else:
        raise ValueError("error arm")


moving = False
moving_thread = None


def keep_moving(direction):
    global moving
    while moving:
        if direction == 'forward':
            move.go_straight(0.18)
        elif direction == 'backward':
            move.go_back(-0.15)
        elif direction == 'left':
            move.turn_left(0.3)
        elif direction == 'right':
            move.turn_right(-0.3)
        time.sleep(0.05)  # 控制发送频率


def control_move(x, y):
    global last_move_cmd, moving, moving_thread
    with move_lock:
        if y < 50:
            if last_move_cmd != 'forward':
                moving = False
                if moving_thread: moving_thread.join()
                moving = True
                moving_thread = threading.Thread(target=keep_moving, args=('forward',))
                moving_thread.start()
                last_move_cmd = 'forward'

        elif y > 200:
            if last_move_cmd != 'backward':
                moving = False
                if moving_thread: moving_thread.join()
                moving = True
                moving_thread = threading.Thread(target=keep_moving, args=('backward',))
                moving_thread.start()
                last_move_cmd = 'backward'

        elif x > 200:
            if last_move_cmd != 'left':
                moving = False
                if moving_thread: moving_thread.join()
                moving = True
                moving_thread = threading.Thread(target=keep_moving, args=('left',))
                moving_thread.start()
                last_move_cmd = 'left'

        elif x < 50:
            if last_move_cmd != 'right':
                moving = False
                if moving_thread: moving_thread.join()
                moving = True
                moving_thread = threading.Thread(target=keep_moving, args=('right',))
                moving_thread.start()
                last_move_cmd = 'right'

        elif 50 < y < 200 and 50 < x < 200:
            if last_move_cmd != 'stop':
                moving = False
                move.stop()
                last_move_cmd = 'stop'


def stop():
    global last_move_cmd
    with move_lock:
        if last_move_cmd != 'stop':
            move.stop()
            last_move_cmd = 'stop'


def control_arm(arm):
    global last_rotation_cmd
    while True:
        if arm == 1:
            arm_data = obj.get_arm_data(2)
            mc = mr
            mercury_list = [
                arm_data[0], -arm_data[1] + 10, arm_data[2],
                -arm_data[3], arm_data[4], 135 + arm_data[5], arm_data[6] - 20
            ]

        elif arm == 2:
            arm_data = obj.get_arm_data(1)
            x, y = arm_data[11], arm_data[12]
            mc = ml
            threading.Thread(target=control_move, args=(x, y,)).start()
            mercury_list = [
                arm_data[0], -arm_data[1] + 10, arm_data[2],
                -arm_data[3], arm_data[4], 135 + arm_data[5], arm_data[6] + 20
            ]

        else:
            raise ValueError("error arm")

        red_btn = arm_data[9]
        blue_btn = arm_data[10]
        atom_btn = arm_data[7]
        if red_btn == 0:
            threading.Thread(target=control_gripper, args=(mc, 1,)).start()

        elif blue_btn == 0:
            threading.Thread(target=control_gripper, args=(mc, 2,)).start()

        if red_btn == 0 and blue_btn == 0:
            time.sleep(0.01)
            continue

        if atom_btn == 0:
            exit()

        mc.send_angles(mercury_list, 6, _async=True)
        time.sleep(0.01)


def main():
    threading.Thread(target=control_arm, args=(1,)).start()  # 左臂
    threading.Thread(target=control_arm, args=(2,)).start()  # 右臂
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()

```

---

---
