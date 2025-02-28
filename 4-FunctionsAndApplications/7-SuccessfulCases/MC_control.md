# MyController S570 Control M750 Program Example

### Connect the exoskeleton and two MyArm M750 robots to the PC via USB, and run the following script.
**Note: Ensure each serial port corresponds to the correct device; The three joints of the exoskeleton are rotated 90 degrees and fixed**  
<video src="../../resources/7-SuccessfulCases/attention.mp4" controls="controls" width="800" height="500"></video>  

**Note 2: Before using MyArmM750, you can determine whether the rotation direction of each joint of MyArmM750 matches the rotation direction of the exoskeleton by setting mercury_list = [] to 0 in turn**  

```
For example:
"mercury_list = [arm_data[1], 0, 0, 0, 0, 0, 0]"
After running the program, if joint 2 of the MyArmM750 rotates in the opposite direction to joint 1 of the exoskeleton, it needs to be reversed
Other joints are judged in turn
```

```bash
# Control script
import threading
from pymycobot import Mercury, MyArmM
from exoskeleton_api import exoskeleton

obj = exoskeleton(port="COM15")  # Exoskeleton serial port
ml = MyArmM("COM41", 1000000)  # Left M750 arm serial port
mr = MyArmM("COM36", 1000000)  # Right M750 arm serial port


# 0 Left arm, 1 Right arm
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


# Left arm
threading.Thread(target=control_arm, args=(0,)).start()
# Right arm
threading.Thread(target=control_arm, args=(1,)).start()
```


### Once the program runs successfully, the MyArm M750 can be controlled with the exoskeleton
<video src="../../resources/7-SuccessfulCases/s570.mp4" controls="controls" width="800" height="500"></video>


---



---