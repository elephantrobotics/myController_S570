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
import time
from pymycobot import Mercury, MyArmM
from pymycobot import ExoskeletonSocket, Exoskeleton


# Initialize Devices
# obj = Exoskeleton(port="COM15")  # Exoskeleton serial port
obj = ExoskeletonSocket("192.168.4.1", 80)  # Exoskeleton Wi-Fi connection
ml = MyArmM("COM5", 1000000)  # Left M750 arm serial port
mr = MyArmM("COM5", 1000000)  # Right M750 arm serial port

# ========== Joint Limit Configuration ==========
# Fill in according to the provided parameters (Units: degrees)
# Format: (Minimum Value, Maximum Value)
JOINT_LIMITS = [
(-163, 163),  # Joint 1
(-58, 93),  # Joint 2
(-90, 73),  # Joint 3
(-150, 148),  # Joint 4
(-89, 85),  # Joint 5
(-148, 148),  # Joint 6
(-116, 0),  # Joint 7 (Gripper)
]

# Gripper Angle Definitions
GRIPPER_CLOSE = -116  # Closed
GRIPPER_OPEN = 0  # Open


def clamp_angles(angles):
"""
Clamps a list of angles within the safe operating range.
Angles exceeding the limits are clamped to the nearest boundary value.
"""
clamped = []
for i, angle in enumerate(angles):
if i >= len(JOINT_LIMITS):
clamped.append(angle)
continue

low, high = JOINT_LIMITS[i]

if angle < low:
print(f"Joint {i + 1} angle {angle:.1f}° is below the lower limit of {low}°; clamped to {low}°.")
clamped.append(low)
elif angle > high:
print(f"Joint {i + 1} Angle {angle:.1f}° exceeds upper limit {high}°; clamped to {high}°")
clamped.append(high)
else:
clamped.append(angle)

return clamped


def check_joints_limits(angles):
"""
Checks if all joint angles are within their limits.
Returns: (is_all_valid, list_of_clamped_angles)
"""
all_valid = True
clamped = []

for i, angle in enumerate(angles):
if i >= len(JOINT_LIMITS):
clamped.append(angle)
continue

low, high = JOINT_LIMITS[i]

if angle < low or angle > high:
print(f"Joint {i + 1} angle {angle:.1f}° exceeds limit range [{low}°, {high}°]")
all_valid = False

# Clamp the angle
clamped_angle = max(min(angle, high), low)
clamped.append(clamped_angle)

return all_valid, clamped

def control_arm(arm):
"""
arm: 1 for Left Arm, 2 for Right Arm
"""
while True:
try:
if arm == 1:
arm_data = obj.get_arm_data(1)
print("l: ", arm_data)
mc = ml

# Calculate target angles based on exoskeleton data
# Adjust according to the actual mapping relationship
mercury_list = [
arm_data[1] + 70,
-arm_data[0],
arm_data[3],
arm_data[4]-90,
-arm_data[5] + 50,
arm_data[6],
0
]


# ========== Gripper Control ==========
if arm_data[10] == 1:
mercury_list[6] = GRIPPER_CLOSE
print("Gripper Closing")
elif arm_data[11] == 1:
mercury_list[6] = GRIPPER_OPEN
print("Gripper Opening")

# If both buttons are pressed simultaneously, skip this iteration
if len(arm_data) > 7 and arm_data[6] == 0 and arm_data[7] == 0:
print("Both buttons pressed simultaneously; skipping this iteration.")
time.sleep(0.01)
continue

elif arm == 2:
arm_data = obj.get_arm_data(2)
print("r: ", arm_data)
mc = mr

# Calculate target angles based on exoskeleton data
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
print("Gripper closing.")
elif  arm_data[11] == 1:
mercury_list[6] = GRIPPER_OPEN
print("Gripper opening.")

# If both buttons are pressed simultaneously, skip this iteration
if len(arm_data) > 7 and arm_data[6] == 0 and arm_data[7] == 0:
print("Both buttons pressed simultaneously; skipping this iteration.")
time.sleep(0.01)
continue
else:
raise ValueError("Invalid arm: 1 for Left Arm, 2 for Right Arm.")

# ========== Limit Check ==========
all_valid, clamped_list = check_joints_limits(mercury_list)

# Always send the corrected angles (to ensure limits are not exceeded)
mc.set_joints_angle(clamped_list, 10)

if all_valid:
print(f"Command sent: {[round(a, 1) for a in clamped_list]}")
else:
print(f"Sent after correction: {[round(a, 1) for a in clamped_list]}")

time.sleep(0.01)

except Exception as e:
print(f"Control loop exception: {e}")
time.sleep(0.1)


# Start control threads for the left and right arms
threading.Thread(target=control_arm, args=(1,), daemon=True).start()  # Left arm
threading.Thread(target=control_arm, args=(2,), daemon=True).start()  # Right arm

# Keep the main thread running
try:
while True:
time.sleep(1)
except KeyboardInterrupt:
print("Program terminated.")
```


### Once the program runs successfully, the MyArm M750 can be controlled with the exoskeleton
<video src="../../resources/7-SuccessfulCases/s570.mp4" controls="controls" width="800" height="500"></video>


---



---
