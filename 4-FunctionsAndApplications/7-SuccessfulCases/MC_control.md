# MyController S570 控制M750程序案例

### 将外骨骼和两台MyArm M750通过USB的方式连接上PC端，并保存运行以下脚本文件。
**注意：确保每个串口号对应的设备是正确的**

```bash
import threading
from pymycobot import Mercury, MyArmM
from exoskeleton_api import exoskeleton

obj = exoskeleton(port="COM15")  # 外骨骼串口号
ml = MyArmM("COM41", 1000000)  # 左M750臂串口号
mr = MyArmM("COM36", 1000000)  # 右M750臂串口号



# 0 左臂，1 右臂
def control_arm(arm):
    # global angle
    while True:
        if arm == 0:
            arm_data = obj.get_data(0)
            print("l: ", arm_data)
            mc = ml
            # mc = mr
            mercury_list = [
                arm_data[1] + 70, -arm_data[0], arm_data[3], arm_data[4],
                -arm_data[5] + 50, arm_data[6], 0
            ]
            # 设置夹爪角度，忽略返回值异常
            if arm_data[7] == 0:
                try:
                    # mc.set_joint_angle(7, -100, 100)  # 设置夹爪角度为 -100
                    mercury_list[6] = -100
                    # angle = -100
                except Exception as e:
                    print(f"Warning: Failed to set angle -100. Error: {e}")
                    # angle = -100  # 即使失败也设置默认值

            elif arm_data[8] == 0:
                try:
                    # mc.set_joint_angle(7, 0, 100)  # 设置夹爪角度为 0
                    mercury_list[6] = 0
                    # angle = 0
                except Exception as e:
                    print(f"Warning: Failed to set angle 0. Error: {e}")
                    # angle = 0  # 即使失败也设置默认值
        elif arm == 1:
            arm_data = obj.get_data(1)
            print("r: ", arm_data)
            mc = mr

            mercury_list = [
                -arm_data[1] - 50, arm_data[0], arm_data[3], arm_data[4],
                -arm_data[5] + 50, arm_data[6], 0
            ]
            # 设置夹爪角度，忽略返回值异常
            if arm_data[7] == 0:
                try:
                    # mc.set_joint_angle(7, -100, 100)  # 设置夹爪角度为 -100
                    mercury_list[6] = -100
                    # angle = -100
                except Exception as e:
                    print(f"Warning: Failed to set angle -100. Error: {e}")
                    # angle = -100  # 即使失败也设置默认值

            elif arm_data[8] == 0:
                try:
                    # mc.set_joint_angle(7, 0, 100)  # 设置夹爪角度为 0
                    mercury_list[6] = 0
                    # angle = 0
                except Exception as e:
                    print(f"Warning: Failed to set angle 0. Error: {e}")
                    # angle = 0  # 即使失败也设置默认值
        else:
            raise ValueError("error arm")

        print(mercury_list)
        try:
            mc.set_joints_angle(mercury_list, 50)
        except:
            pass


# 左臂
threading.Thread(target=control_arm, args=(0,)).start()
# 右臂
threading.Thread(target=control_arm, args=(1,)).start()

```

### 程序成功运行之后即可用外骨骼控制MyArm M750
<video src="../../resources/7-SuccessfulCases/s570.mp4" controls="controls" width="800" height="500"></video>


---



---