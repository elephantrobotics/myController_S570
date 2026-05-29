# MyController S570 控制M750程序案例

### 将外骨骼和两台MyArm M750通过USB的方式连接上PC端，并保存运行以下脚本文件。
**注意1：确保每个串口号对应的设备是正确的；将外骨骼的三关节旋转九十度后固定**  
<video src="../../resources/7-SuccessfulCases/attention.mp4" controls="controls" width="800" height="500"></video>

**注意2：在用MyArmM750之前可通过依次将 mercury_list = []中的元素设置为0，来判断MyArmM750的每个关节旋转方向是否匹配外骨骼的旋转方向**
*** ***

```python
例如：
mercury_list = [arm_data[1], 0, 0, 0, 0, 0, 0]
运行程序后，若MyArmM750的关节2与外骨骼的关节1旋转方向相反，则需要取反
其他关节依次判断
```


```bash
# 控制脚本
import threading
import time
from pymycobot import Mercury, MyArmM
from pymycobot import ExoskeletonSocket,Exoskeleton


# 初始化设备
#obj = Exoskeleton(port="COM15")  # 外骨骼串口号
obj = ExoskeletonSocket("192.168.4.1", 80)  # 外骨骼 Wi-Fi 连接
ml = MyArmM("COM5", 1000000)  # 左M750臂串口号
mr = MyArmM("COM5", 1000000)  # 右M750臂串口号

# ========== 关节限位配置 ==========
# 根据提供的参数填写（单位：度）
# 格式：(最小值, 最大值)
JOINT_LIMITS = [
    (-163, 163),  # 关节1
    (-58, 93),  # 关节2
    (-90, 73),  # 关节3
    (-150, 148),  # 关节4
    (-89, 85),  # 关节5
    (-148, 148),  # 关节6
    (-116, 0),  # 关节7（夹爪）
]

# 夹爪角度定义
GRIPPER_CLOSE = -116  # 闭合
GRIPPER_OPEN = 0  # 张开


def clamp_angles(angles):
    """
    将角度列表限制在安全范围内
    超出限位的角度会被钳制到最近的边界值
    """
    clamped = []
    for i, angle in enumerate(angles):
        if i >= len(JOINT_LIMITS):
            clamped.append(angle)
            continue

        low, high = JOINT_LIMITS[i]

        if angle < low:
            print(f"⚠️ 关节{i + 1} 角度 {angle:.1f}° 低于下限 {low}°，已限制为 {low}°")
            clamped.append(low)
        elif angle > high:
            print(f"⚠️ 关节{i + 1} 角度 {angle:.1f}° 超过上限 {high}°，已限制为 {high}°")
            clamped.append(high)
        else:
            clamped.append(angle)

    return clamped


def check_joints_limits(angles):
    """
    检查所有关节角度是否在限位内
    返回 (是否全部合法, 修正后的角度列表)
    """
    all_valid = True
    clamped = []

    for i, angle in enumerate(angles):
        if i >= len(JOINT_LIMITS):
            clamped.append(angle)
            continue

        low, high = JOINT_LIMITS[i]

        if angle < low or angle > high:
            print(f"❌ 关节{i + 1} 角度 {angle:.1f}° 超出限位范围 [{low}°, {high}°]")
            all_valid = False

        # 钳制角度
        clamped_angle = max(min(angle, high), low)
        clamped.append(clamped_angle)

    return all_valid, clamped

def control_arm(arm):
    """
    arm: 1 左臂, 2 右臂
    """
    while True:
        try:
            if arm == 1:
                arm_data = obj.get_arm_data(1)
                print("l: ", arm_data)
                mc = ml

                # 根据外骨骼数据计算目标角度
                # 根据实际映射关系调整
                mercury_list = [
                    arm_data[1] + 70,
                    -arm_data[0],
                    arm_data[3],
                    arm_data[4]-90,
                    -arm_data[5] + 50,
                    arm_data[6],
                    0
                ]


                # ========== 夹爪控制 ==========
                if arm_data[10] == 1:
                    mercury_list[6] = GRIPPER_CLOSE
                    print("🔧 夹爪闭合")
                elif  arm_data[11] == 1:
                    mercury_list[6] = GRIPPER_OPEN
                    print("🔧 夹爪张开")

                # 如果两个按钮同时按下，跳过本次
                if len(arm_data) > 7 and arm_data[6] == 0 and arm_data[7] == 0:
                    print("⚠️ 两个按钮同时按下，跳过本次")
                    time.sleep(0.01)
                    continue

            elif arm == 2:
                arm_data = obj.get_arm_data(2)
                print("r: ", arm_data)
                mc = mr

                # 根据外骨骼数据计算目标角度
                mercury_list = [
                    -arm_data[1] - 50,
                    -arm_data[0],
                    arm_data[3]-10,
                    arm_data[4]+90,
                    -arm_data[5] + 50,
                    arm_data[6], 0
                ]


                if arm_data[10] == 1:
                    mercury_list[6] = GRIPPER_CLOSE
                    print("🔧 夹爪闭合")
                elif  arm_data[11] == 1:
                    mercury_list[6] = GRIPPER_OPEN
                    print("🔧 夹爪张开")

                # 如果两个按钮同时按下，跳过本次
                if len(arm_data) > 7 and arm_data[6] == 0 and arm_data[7] == 0:
                    print("⚠️ 两个按钮同时按下，跳过本次")
                    time.sleep(0.01)
                    continue
            else:
                raise ValueError("error arm: 1 左臂, 2 右臂")

            # ========== 限位检查 ==========
            all_valid, clamped_list = check_joints_limits(mercury_list)

            # 始终使用修正后的角度发送（确保不超限）
            mc.set_joints_angle(clamped_list, 10)

            if all_valid:
                print(f"✅ 指令已发送: {[round(a, 1) for a in clamped_list]}")
            else:
                print(f"⚠️ 已修正后发送: {[round(a, 1) for a in clamped_list]}")

            time.sleep(0.01)

        except Exception as e:
            print(f"控制循环异常: {e}")
            time.sleep(0.1)


# 启动左右臂控制线程
threading.Thread(target=control_arm, args=(1,), daemon=True).start()  # 左臂
threading.Thread(target=control_arm, args=(2,), daemon=True).start()  # 右臂

# 保持主线程运行
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("程序已退出")

```

### 程序成功运行之后即可用外骨骼控制MyArm M750
<video src="../../resources/7-SuccessfulCases/s570.mp4" controls="controls" width="800" height="500"></video>


---



---
