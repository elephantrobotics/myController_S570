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
from pymycobot import Mercury, MyArmM
from pymycobot import Exoskeleton

obj = Exoskeleton(port="COM15")  # 外骨骼串口号
ml = MyArmM("COM41", 1000000)  # 左M750臂串口号
mr = MyArmM("COM36", 1000000)  # 右M750臂串口号



# 0 左臂，1 右臂
def control_arm(arm):
    while True:
        if arm == 0:
            arm_data = obj.get_data(0)
            print("l: ", arm_data)
            mc = ml
            mercury_list = [
                arm_data[1] + 70, -arm_data[0], arm_data[3], arm_data[4],
                -arm_data[5] + 50, arm_data[6], 0
            ]
            # 设置夹爪角度，忽略返回值异常
            if arm_data[7] == 0:
                try:
                    mercury_list[6] = -100
                except Exception as e:
                    print(f"Warning: Failed to set angle -100. Error: {e}")

            elif arm_data[8] == 0:
                try:
                    mercury_list[6] = 0
                except Exception as e:
                    print(f"Warning: Failed to set angle 0. Error: {e}")
            try:
                mc.set_joints_angle(mercury_list, 10)
                time.sleep(0.01)
            except:
                pass
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
                    mercury_list[6] = -100
                except Exception as e:
                    print(f"Warning: Failed to set angle -100. Error: {e}")

            elif arm_data[8] == 0:
                try:
                    mercury_list[6] = 0
                except Exception as e:
                    print(f"Warning: Failed to set angle 0. Error: {e}")

            try:
                mc.set_joints_angle(mercury_list, 10)
                time.sleep(0.01)
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