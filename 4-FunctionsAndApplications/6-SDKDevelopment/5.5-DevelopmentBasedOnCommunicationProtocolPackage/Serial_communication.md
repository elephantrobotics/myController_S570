# Communication and Message Commands

> **Notice:** Before communicating directly through the communication protocol, it is necessary to burn the latest firmware of the exoskeleton on BASIC and burn the latest ATOM firmware

| Please read the interface protocol document in detail and proceed with your program development after testing. |
| -------------------------------------------------------------------------------------------------------------- |

## 1 Settings of USB Communication

**_Make sure the following settings are prepared:_**

- Interface of mainline: USB Type-C connection PC and Basic
- Port ratio: 1000000
- Data bit: 8
- Parity bit: none
- Stop bit: 1

## 2 Introduction to Command Frame & Sole Instruction

The PC transmits data through BASIC, and the robotic arm decodes the data into commands with return values and uses serial communication protocol to send the results back to the PC through BASIC within 5 milliseconds. The communication frequency can reach 200Hz.

## 3 Formats of Message Commands' Sending and Receiving

Both sending and receiving should be represented in hexadecimal. Each command should contain 5 parts as shown below. Part 3 and 4 can be left a blank.

- 1 Pin of command: 0xFE 0xFE
  - Invariable
  - Indispensable
- 2 Effective lengthen:
  - Aggregated length including pin, serial number, functional codes and end
  - Indispensable
- 3 Serial number: 00 ~ 8F
  - Corresponding number of developed commands
  - You may leave it blank.
- 4 Functional codes:
  - Purpose-oriented
  - You may leave it blank.
- 5 End: 0XFA
  - Invariable
  - Indispensable

## 4 Explanation for Commands

| Type          | Data               | Length | Function                                               |
| ------------- | ------------------ | ------ | ------------------------------------------------------ |
| Command Frame | start bit: 0       | 1      | Head frame identification, 0XFE                        |
|               | start bit: 1       | 1      | Head frame identification, 0XFE                        |
|               | bit of data length | 1      | Different commands correspond to different data length |
|               | command bit        | 1      | depending on different commands                        |
| Command Frame | data               | 0-16   | commands with data, depending on different commands    |
| End Frame     | end bit            | 1      | stop bit, 0XFA                                         |

## 5 Explanation for Sole-Instruction Commands

### Read all data of both arms.

| Domain  | Explanation          | Data |
| :------ | :------------------- | :--- |
| Data[0] | identification frame | 0XFE |
| Data[1] | identification frame | 0XFE |
| Data[2] | data-length frame    | 0X02 |
| Data[3] | command frame        | 0X01 |
| Data[4] | end frame            | 0XFA |

Example:

Port transmission: FE FE 02 01 FA

Return value: data structure

| Data Domain | Description                                          | Data                                                                            |
| :---------- | :--------------------------------------------------- | :------------------------------------------------------------------------------ |
| Data[0]     | Return value: Recognition frame                      | 0XFE                                                                            |
| Data[1]     | Return value: Recognition frame                      | 0XFE                                                                            |
| Data[2]     | Return value: Return length                          | 0X3C                                                                            |
| Data[3]     | Return value: Command frame                          | 0X01                                                                            |
| Data[4]     | Return value: Left arm joint 1 high                  | Left_Servo1_high                                                                |
| Data[5]     | Return value: Left arm joint 1 low position          | Left_Servo1_Low                                                                 |
| Data[6]     | Return value: Left arm joint 2 high                  | Left_Servo2_high                                                                |
| Data[7]     | Return value: Left arm joint 2 low                   | Left_Servo2_Low                                                                 |
| Data[8]     | Return value: Left arm joint 3 high                  | Left_Servo3_high                                                                |
| Data[9]     | Return value: Left arm joint 3 low position          | Left_Servo3_Low                                                                 |
| Data[10]    | Return value: Left arm joint 4 high                  | Left_Servo4_high                                                                |
| Data[11]    | Return value: Left arm joint 4 low position          | Left_Servo4_Low                                                                 |
| Data[12]    | Return value: Left arm joint 5 high                  | Left_Servo5_high                                                                |
| Data[13]    | Return value: Left arm joint 5 low position          | Left_Servo5_Low                                                                 |
| Data[14]    | Return value: Left arm joint 6 high                  | Left_Servo6_high                                                                |
| Data[15]    | Return value: Left arm joint 6 low position          | Left_Servo6_Low                                                                 |
| Data[16]    | Return value: Left arm joint 7 high                  | Left_Servo7_High                                                                |
| Data[17]    | Return value: Left arm joint 7 low position          | Left_Servo7_Low                                                                 |
| Data[18]    | Return value: Left Arm remote sensing button status  | Left_button_status (bit1: Remote sensing button bit2: Button 1 bit3: Button 2)  |
| Data[19]    | Return value: Left Arm remote sensing x value        | Left_remote_sensing_x-value                                                     |
| Data[20]    | Return value: Left Arm remote sensing y value        | Left_remote_sensing_y-value                                                     |
| Data[21]    | Return value: Right arm Joint 1 high                 | Right_Servo1_high                                                               |
| Data[22]    | Return value: Right arm joint 1 low position         | Right_Servo1_Low                                                                |
| Data[23]    | Return value: Right arm joint 2 high                 | Right_Servo2_high                                                               |
| Data[24]    | Return value: Right arm joint 2 low position         | Right_Servo2_Low                                                                |
| Data[25]    | Return value: Right arm joint 3 high                 | Right_Servo3_high                                                               |
| Data[26]    | Return value: Right arm joint 3 low position         | Right_Servo3_Low                                                                |
| Data[27]    | Return value: Right arm joint 4 high                 | Right_Servo4_high                                                               |
| Data[28]    | Return value: Right arm joint 4 low position         | Right_Servo4_Low                                                                |
| Data[29]    | Return value: Right arm joint 5 high                 | Right_Servo5_high                                                               |
| Data[30]    | Return value: Right arm joint 5 low position         | Right_Servo5_Low                                                                |
| Data[31]    | Return value: Right arm joint 6 high                 | Right_Servo6_high                                                               |
| Data[32]    | Return value: Right arm joint 6 low position         | Right_Servo6_Low                                                                |
| Data[33]    | Return value: Right arm joint 7 high                 | Right_Servo7_High                                                               |
| Data[34]    | Return value: Right arm joint 7 low position         | Right_Servo7_Low                                                                |
| Data[35]    | Return value: Right Arm remote sensing button status | Right_button_status (bit1: Remote sensing button bit2: Button 1 bit3: Button 2) |
| Data[36]    | Return value: Right Arm remote sensing x value       | Right_remote_sensing_x-value                                                    |
| Data[37]    | Return value: Right Arm remote sensing Y-value       | Right_remote_sensing_y-value                                                    |
| Data[38]    | Return value: Left arm X-axis high                   | Right_Servo2_high                                                               |
| Data[39]    | Return value: Left arm X-axis low                    | Right_Servo2_Low                                                                |
| Data[40]    | Return value: High Y-axis of the left arm            | Right_Servo3_high                                                               |
| Data[41]    | Return value: Low Y-axis of the left arm             | Right_Servo3_Low                                                                |
| Data[42]    | Return value: Left arm Z-axis high                   | Right_Servo4_high                                                               |
| Data[43]    | Return value: Low Z-axis of the left arm             | Right_Servo4_Low                                                                |
| Data[44]    | Return value: Left arm rx rotation high              | Right_Servo5_high                                                               |
| Data[45]    | Return value: Left arm rx rotation low position      | Right_Servo5_Low                                                                |
| Data[46]    | Return value: Left arm ry rotation high              | Right_Servo6_high                                                               |
| Data[47]    | Return value: Left arm ry rotation low position      | Right_Servo6_Low                                                                |
| Data[48]    | Return value: Left arm rz rotation high              | Right_Servo7_High                                                               |
| Data[49]    | Return value: Left arm rz rotation low position      | Right_Servo7_Low                                                                |
| Data[50]    | Return value: Right arm X-axis high                  | Right_Servo2_high                                                               |

Example:

Assuming Atom has successfully connected：

Return value of port：FE FE 24 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FA

---

### Read all data from a single arm

| Domain  | Explanation          | Data                   |
| :------ | :------------------- | :--------------------- |
| Data[0] | identification frame | 0XFE                   |
| Data[1] | identification frame | 0XFE                   |
| Data[2] | data-length frame    | 0X03                   |
| Data[3] | command frame        | 0X02                   |
| Data[4] | Specify a single arm | 0x01(Left)/0x02(Right) |
| Data[5] | end frame            | 0XFA                   |

Example:

Port transmission: FE FE 03 02 01 FA

Return value: data structure

| Data Domain | Description                                         | Data                                                                           |
| :---------- | :-------------------------------------------------- | :----------------------------------------------------------------------------- |
| Data[0]     | Return value: Recognition frame                     | 0XFE                                                                           |
| Data[1]     | Return value: Recognition frame                     | 0XFE                                                                           |
| Data[2]     | Return value: Return length                         | 0X13                                                                           |
| Data[3]     | Return value: Command frame                         | 0X02                                                                           |
| Data[4]     | Return value: Left arm joint 1 high                 | Left_Servo1_high                                                               |
| Data[5]     | Return value: Left arm joint 1 low position         | Left_Servo1_Low                                                                |
| Data[6]     | Return value: Left arm joint 2 high                 | Left_Servo2_high                                                               |
| Data[7]     | Return value: Left arm joint 2 low                  | Left_Servo2_Low                                                                |
| Data[8]     | Return value: Left arm joint 3 high                 | Left_Servo3_high                                                               |
| Data[9]     | Return value: Left arm joint 3 low position         | Left_Servo3_Low                                                                |
| Data[10]    | Return value: Left arm joint 4 high                 | Left_Servo4_high                                                               |
| Data[11]    | Return value: Left arm joint 4 low position         | Left_Servo4_Low                                                                |
| Data[12]    | Return value: Left arm joint 5 high                 | Left_Servo5_high                                                               |
| Data[13]    | Return value: Left arm joint 5 low position         | Left_Servo5_Low                                                                |
| Data[14]    | Return value: Left arm joint 6 high                 | Left_Servo6_high                                                               |
| Data[15]    | Return value: Left arm joint 6 low position         | Left_Servo6_Low                                                                |
| Data[16]    | Return value: Left arm joint 7 high                 | Left_Servo7_High                                                               |
| Data[17]    | Return value: Left arm joint 7 low position         | Left_Servo7_Low                                                                |
| Data[18]    | Return value: Left Arm remote sensing button status | Left_button_status (bit1: Remote sensing button bit2: Button 1 bit3: Button 2) |
| Data[19]    | Return value: Left Arm remote sensing x value       | Left_remote_sensing_x-value                                                    |
| Data[20]    | Return value: Left Arm remote sensing y value       | Left_remote_sensing_y-value                                                    |
| Data[21]    | Return value: Left arm X-axis high                  | Right_Servo2_high                                                              |
| Data[22]    | Return value: Left arm X-axis low                   | Right_Servo2_Low                                                               |
| Data[23]    | Return value: High Y-axis of the left arm           | Right_Servo3_high                                                              |
| Data[24]    | Return value: Low Y-axis of the left arm            | Right_Servo3_Low                                                               |
| Data[25]    | Return value: Left arm Z-axis high                  | Right_Servo4_high                                                              |
| Data[26]    | Return value: Low Z-axis of the left arm            | Right_Servo4_Low                                                               |
| Data[27]    | Return value: Left arm rx rotation high             | Right_Servo5_high                                                              |
| Data[28]    | Return value: Left arm rx rotation low position     | Right_Servo5_Low                                                               |
| Data[29]    | Return value: Left arm ry rotation high             | Right_Servo6_high                                                              |
| Data[30]    | Return value: Left arm ry rotation low position     | Right_Servo6_Low                                                               |
| Data[31]    | Return value: Left arm rz rotation high             | Right_Servo7_High                                                              |
| Data[32]    | Return value: Left arm rz rotation low position     | Right_Servo7_Low                                                               |
| Data[33]    | End frame                                           | 0XFA                                                                           |

Example:

Assuming Atom has successfully connected：

Return value of port：FE FE 13 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FA

---

### Read data from a single encoder of a single arm

| Domain  | Explanation             | Data                   |
| :------ | :---------------------- | :--------------------- |
| Data[0] | identification frame    | 0XFE                   |
| Data[1] | identification frame    | 0XFE                   |
| Data[2] | data-length frame       | 0X04                   |
| Data[3] | command frame           | 0X03                   |
| Data[4] | Specify a single arm    | 0x01(Left)/0x02(Right) |
| Data[5] | Specify the servo motor | Joint_id (1-7)         |
| Data[6] | end frame               | 0XFA                   |

Example:

Port transmission：FE FE 04 03 01 01 FA

Return value: data structure

| Domain  | Explanation                        | Data               |
| :------ | :--------------------------------- | :----------------- |
| Data[0] | return value: identification frame | 0XFE               |
| Data[1] | return value: identification frame | 0XFE               |
| Data[2] | return value: data-length frame    | 0X04               |
| Data[3] | return value: command frame        | 0X03               |
| Data[4] | high angle of steering gear        | Servo_Encoder_High |
| Data[5] | low angle of No.1 steering gear    | Servo_Encoder_Low  |
| Data[6] | end frame                          | 0XFA               |

Example:

Assuming Atom has successfully connected：

Return value of port：FE FE 04 03 08 00 FA

---

### Set zero point

| Domain  | Explanation             | Data                   |
| :------ | :---------------------- | :--------------------- |
| Data[0] | identification frame    | 0XFE                   |
| Data[1] | identification frame    | 0XFE                   |
| Data[2] | data-length frame       | 0X04                   |
| Data[3] | command frame           | 0X04                   |
| Data[4] | Specify a single arm    | 0x01(Left)/0x02(Right) |
| Data[5] | Specify the servo motor | Joint_id (1-7)         |
| Data[6] | end frame               | 0XFA                   |

Example:

Port transmission：FE FE 04 04 01 01 FA

Return value: Data structure

| Data Domain | Description                     | Data |
| :---------- | :------------------------------ | :--- |
| Data[0]     | Return value: Recognition frame | 0XFE |
| Data[1]     | Return value: Recognition frame | 0XFE |
| Data[2]     | Return value: Return length     | 0X03 |
| Data[3]     | Return value: Command frame     | 0X04 |
| Data[4]     | Return value: 1                 | 1    |
| Data[5]     | End character                   | 0XFA |

Example:

Port return: FE FE 03 04 01 FA

---

### Set the RGB values of the LED lights

| Domain  | Explanation            | Data                   |
| :------ | :--------------------- | :--------------------- |
| Data[0] | identification frame   | 0XFE                   |
| Data[1] | identification frame   | 0XFE                   |
| Data[2] | data-length frame      | 0X06                   |
| Data[3] | command frame          | 0X05                   |
| Data[4] | Specify a single arm   | 0x01(Left)/0x02(Right) |
| Data[5] | Red proportion value   | R_Value                |
| Data[6] | Green proportion value | G_Value                |
| Data[7] | Blue proportion value  | B_Value                |
| Data[8] | end frame              | 0XFA                   |

Example:

Port transmission：FE FE 06 05 01 00 FF 00 FA

Return value: Data structure

| Data Domain | Description                     | Data |
| :---------- | :------------------------------ | :--- |
| Data[0]     | Return value: Recognition frame | 0XFE |
| Data[1]     | Return value: Recognition frame | 0XFE |
| Data[2]     | Return value: Return length     | 0X03 |
| Data[3]     | Return value: Command frame     | 0X05 |
| Data[4]     | Return value: 1                 | 1    |
| Data[5]     | End character                   | 0XFA |

Example:

Port return: FE FE 03 05 01 FA

Read the version number of the basic firmware

| Data Domain | Description          | Data |
| :---------- | :------------------- | :--- |
| Data[0]     | Identification frame | 0XFE |
| Data[1]     | Identification Frame | 0XFE |
| Data[2]     | Data Length frame    | 0X02 |
| Data[3]     | Instruction Frame    | 0X06 |
| Data[4]     | End frame            | 0XFA |

Example:

Serial port transmission: FE FE 02 06 FA

Return value: Data structure

| Data Domain | Description                                | Data |
| :---------- | :----------------------------------------- | :--- |
| Data[0]     | Return value: Recognition frame            | 0XFE |
| Data[1]     | Return value: Recognition frame            | 0XFE |
| Data[2]     | Return value: Return length                | 0X03 |
| Data[3]     | Return value: Command frame                | 0X06 |
| Data[4]     | Return value: Firmware version number \*10 | 0x0C |
| Data[5]     | End character                              | 0XFA |

Example:

Port returns: FE FE 03 06 0C FA

Read the atom firmware version number

| Data Domain | Description          | Data                   |
| :---------- | :------------------- | :--------------------- |
| Data[0]     | Identification frame | 0XFE                   |
| Data[1]     | Identification Frame | 0XFE                   |
| Data[2]     | Data Length frame    | 0X02                   |
| Data[3]     | Instruction Frame    | 0X07                   |
| Data[4]     | Instruction Frame    | 0x01(left)/0x02(right) |
| Data[5]     | End frame            | 0XFA                   |

Example:

Serial port transmission: FE FE 02 07 01 FA

Return value: Data structure

| Data Domain | Description                                | Data                   |
| :---------- | :----------------------------------------- | :--------------------- |
| Data[0]     | Return value: Recognition frame            | 0XFE                   |
| Data[1]     | Return value: Recognition frame            | 0XFE                   |
| Data[2]     | Return value: Return length                | 0X03                   |
| Data[3]     | Return value: Command frame                | 0X06                   |
| Data[4]     | Instruction Frame                          | 0x01(left)/0x02(right) |
| Data[5]     | Return value: Firmware version number \*10 | 0x0C                   |
| Data[6]     | End character                              | 0XFA                   |

Example:

Port returns: FE FE 04 07 01 0C FA
