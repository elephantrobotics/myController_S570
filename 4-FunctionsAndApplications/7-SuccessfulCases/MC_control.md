# MyController S570 Control M750 Program Example

### Connect the exoskeleton and two MyArm M750 robots to the PC via USB, and run the following script.
**Note: Ensure each serial port corresponds to the correct device.**

```bash
import threading
from pymycobot import Mercury, MyArmM
from exoskeleton_api import exoskeleton

obj = exoskeleton(port="COM15")  # Exoskeleton serial port
ml = MyArmM("COM41", 1000000)  # Left M750 arm serial port
mr = MyArmM("COM36", 1000000)  # Right M750 arm serial port


# 0 Left arm, 1 Right arm
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
            # Set gripper angle, ignore return value exceptions
            if arm_data[7] == 0:
                try:
                    # mc.set_joint_angle(7, -100, 100)  # Set gripper angle to -100
                    mercury_list[6] = -100
                    # angle = -100
                except Exception as e:
                    print(f"Warning: Failed to set angle -100. Error: {e}")
                    # angle = -100  # Set default value even if failed

            elif arm_data[8] == 0:
                try:
                    # mc.set_joint_angle(7, 0, 100)  # Set gripper angle to 0
                    mercury_list[6] = 0
                    # angle = 0
                except Exception as e:
                    print(f"Warning: Failed to set angle 0. Error: {e}")
                    # angle = 0  # Set default value even if failed
        elif arm == 1:
            arm_data = obj.get_data(1)
            print("r: ", arm_data)
            mc = mr

            mercury_list = [
                -arm_data[1] - 50, arm_data[0], arm_data[3], arm_data[4],
                -arm_data[5] + 50, arm_data[6], 0
            ]
            # Set gripper angle, ignore return value exceptions
            if arm_data[7] == 0:
                try:
                    # mc.set_joint_angle(7, -100, 100)  # Set gripper angle to -100
                    mercury_list[6] = -100
                    # angle = -100
                except Exception as e:
                    print(f"Warning: Failed to set angle -100. Error: {e}")
                    # angle = -100  # Set default value even if failed

            elif arm_data[8] == 0:
                try:
                    # mc.set_joint_angle(7, 0, 100)  # Set gripper angle to 0
                    mercury_list[6] = 0
                    # angle = 0
                except Exception as e:
                    print(f"Warning: Failed to set angle 0. Error: {e}")
                    # angle = 0  # Set default value even if failed
        else:
            raise ValueError("error arm")

        print(mercury_list)
        try:
            mc.set_joints_angle(mercury_list, 50)
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