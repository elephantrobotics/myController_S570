# 遥操控制机械臂案例

###  mercury X1(7轴)

双臂协同控制

```python
import threading
from pymycobot import Mercury
from exoskeleton_api import exoskeleton

obj = exoskeleton(port="/dev/ttyACM4")
ml = Mercury("/dev/left_arm")
mr = Mercury("/dev/right_arm")

# 设置双臂为速度融合模式
ml.set_movement_type(2)
mr.set_movement_type(2)
# 设置夹爪运行模式
ml.set_gripper_mode(0)
mr.set_gripper_mode(0)


# 0 左臂，1 右臂
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
        # 由于外骨骼各关节转向、零点与部分机械臂构型不同，在此设置映射关系(根据各关节实际控制转向、位置设置)
        mercury_list = [
            arm_data[0], -arm_data[1], arm_data[2], -arm_data[3], arm_data[4],
            135 + arm_data[5], arm_data[6]
        ]
        # 按键按下控制夹爪开闭
        if arm_data[7] == 0:
            mc.set_gripper_state(1, 100)  
        elif arm_data[8] == 0:
            mc.set_gripper_state(0, 100)
        mc.send_angles(mercury_list, 6)


# 左臂
threading.Thread(target=control_arm, args=(0, )).start()
# 右臂
threading.Thread(target=control_arm, args=(1, )).start()
```


---


[← 上一页](2_API.md) | [下一页 →](4_tracer_API.md)