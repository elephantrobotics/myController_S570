# Communication and Message Commands

> **Notice:** Before communicating directly through the communication protocol, it is necessary to burn the latest firmware of the exoskeleton on BASIC and burn the latest ATOM firmware

| Please read the interface protocol document in detail and proceed with your program development after testing. |
| ------------------------------------------------------------ |

## 1 Settings of USB Communication

***Make sure the following settings are prepared:***

* Interface of mainline: USB Type-C connection PC and Basic
* Port ratio: 115200
* Data bit: 8
* Parity bit: none
* Stop bit: 1



## 2 Introduction to Command Frame & Sole Instruction

The PC transmits data through BASIC, and the robotic arm decodes the data into commands with return values and uses serial communication protocol to send the results back to the PC through BASIC within 5 milliseconds. The communication frequency can reach 200Hz.



## 3 Formats of Message Commands' Sending and Receiving

Both sending and receiving should be represented in hexadecimal. Each command should contain 5 parts as shown below. Part 3 and 4 can be left a blank.

* 1 Pin of command: 0xFE 0xFE
  * Invariable
  * Indispensable
* 2 Effective lengthen:
  * Aggregated length including pin, serial number, functional codes and end
  * Indispensable
* 3 Serial number: 00 ~ 8F
  * Corresponding number of developed commands 
  * You may leave it blank.
* 4 Functional codes:
  * Purpose-oriented
  * You may leave it blank.
* 5 End: 0XFA
  * Invariable
  * Indispensable



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

| Domain   | Explanation                                | Data                                                         |
| :------- | :----------------------------------------- | :----------------------------------------------------------- |
| Data[0]  | return value: identification frame         | 0XFE                                                         |
| Data[1]  | return value: identification frame         | 0XFE                                                         |
| Data[2]  | return value: data-length frame            | 0X24                                                         |
| Data[3]  | return value: command frame                | 0X01                                                         |
| Data[4]  | left arm high angle of No.1 steering gear  | Left_Servo1_high                                             |
| Data[5]  | left arm low  angle of No.1 steering gear  | Left_Servo1_Low                                              |
| Data[6]  | left arm high angle of No.2 steering gear  | Left_Servo2_high                                             |
| Data[7]  | left arm low  angle of No.2 steering gear  | Left_Servo2_Low                                              |
| Data[8]  | left arm high angle of No.3 steering gear  | Left_Servo3_high                                             |
| Data[9]  | left arm low  angle of No.3 steering gear  | Left_Servo3_Low                                              |
| Data[10] | left arm high angle of No.4 steering gear  | Left_Servo4_high                                             |
| Data[11] | left arm low  angle of No.4 steering gear  | Left_Servo4_Low                                              |
| Data[12] | left arm high angle of No.5 steering gear  | Left_Servo5_high                                             |
| Data[13] | left arm low  angle of No.5 steering gear  | Left_Servo5_Low                                              |
| Data[14] | left arm high angle of No.6 steering gear  | Left_Servo6_high                                             |
| Data[15] | left arm low  angle of No.6 steering gear  | Left_Servo6_Low                                              |
| Data[16] | left arm high angle of No.7 steering gear  | Left_Servo7_High                                             |
| Data[17] | left arm low  angle of No.7 steering gear  | Left_Servo7_Low                                              |
| Data[18] | left arm remote sensing button status      | Left_button_status (bit1:remote sensing btn  bit2:btn1  bit3:btn2) |
| Data[19] | left arm remote sensing button x-value     | Left_remote_sensing_x-value                                  |
| Data[20] | left arm remote sensing button y-value     | Left_remote_sensing_y-value                                  |
| Data[21] | right arm high angle of No.7 steering gear | Right_Servo1_high                                            |
| Data[22] | right arm low  angle of No.7 steering gear | Right_Servo1_Low                                             |
| Data[23] | right arm high angle of No.7 steering gear | Right_Servo2_high                                            |
| Data[24] | right arm low  angle of No.7 steering gear | Right_Servo2_Low                                             |
| Data[25] | right arm high angle of No.7 steering gear | Right_Servo3_high                                            |
| Data[26] | right arm low  angle of No.7 steering gear | Right_Servo3_Low                                             |
| Data[27] | right arm high angle of No.7 steering gear | Right_Servo4_high                                            |
| Data[28] | right arm low  angle of No.7 steering gear | Right_Servo4_Low                                             |
| Data[29] | right arm high angle of No.7 steering gear | Right_Servo5_high                                            |
| Data[30] | right arm low  angle of No.7 steering gear | Right_Servo5_Low                                             |
| Data[31] | right arm high angle of No.7 steering gear | Right_Servo6_high                                            |
| Data[32] | right arm low  angle of No.7 steering gear | Right_Servo6_Low                                             |
| Data[33] | right arm high angle of No.7 steering gear | Right_Servo7_High                                            |
| Data[34] | right arm low  angle of No.7 steering gear | Right_Servo7_Low                                             |
| Data[35] | right arm remote sensing button status     | Right_button_status (bit1:remote sensing btn  bit2:btn1  bit3:btn2) |
| Data[36] | right arm remote sensing button x-value    | Right_remote_sensing_x-value                                 |
| Data[37] | right arm remote sensing button x-value    | Right_remote_sensing_y-value                                 |
| Data[38] | end frame                                  | 0XFA                                                         |

Example:

Assuming Atom has successfully connected：

Return value of port：FE FE 24 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 14 00 00 FA

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

| Domain   | Explanation                               | Data                                                         |
| :------- | :---------------------------------------- | :----------------------------------------------------------- |
| Data[0]  | return value: identification frame        | 0XFE                                                         |
| Data[1]  | return value: identification frame        | 0XFE                                                         |
| Data[2]  | return value: data-length frame           | 0X13                                                         |
| Data[3]  | return value: command frame               | 0X02                                                         |
| Data[4]  | left arm high angle of No.1 steering gear | Left_Servo1_high                                             |
| Data[5]  | left arm low  angle of No.1 steering gear | Left_Servo1_Low                                              |
| Data[6]  | left arm high angle of No.2 steering gear | Left_Servo2_high                                             |
| Data[7]  | left arm low  angle of No.2 steering gear | Left_Servo2_Low                                              |
| Data[8]  | left arm high angle of No.3 steering gear | Left_Servo3_high                                             |
| Data[9]  | left arm low  angle of No.3 steering gear | Left_Servo3_Low                                              |
| Data[10] | left arm high angle of No.4 steering gear | Left_Servo4_high                                             |
| Data[11] | left arm low  angle of No.4 steering gear | Left_Servo4_Low                                              |
| Data[12] | left arm high angle of No.5 steering gear | Left_Servo5_high                                             |
| Data[13] | left arm low  angle of No.5 steering gear | Left_Servo5_Low                                              |
| Data[14] | left arm high angle of No.6 steering gear | Left_Servo6_high                                             |
| Data[15] | left arm low  angle of No.6 steering gear | Left_Servo6_Low                                              |
| Data[16] | left arm high angle of No.7 steering gear | Left_Servo7_High                                             |
| Data[17] | left arm low  angle of No.7 steering gear | Left_Servo7_Low                                              |
| Data[18] | left arm remote sensing button status     | Left_button_status (bit1:remote sensing btn  bit2:btn1  bit3:btn2) |
| Data[19] | left arm remote sensing button x-value    | Left_remote_sensing_x-value                                  |
| Data[20] | left arm remote sensing button y-value    | Left_remote_sensing_y-value                                  |
| Data[21] | end frame                                 | 0XFA                                                         |

Example:

Assuming Atom has successfully connected：

Return value of port：FE FE 13 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00 00 FA

---

### Read data from a single encoder of a single arm

| Domain  | Explanation             | Data                   |
| :------ | :---------------------- | :--------------------- |
| Data[0] | identification frame    | 0XFE                   |
| Data[1] | identification frame    | 0XFE                   |
| Data[2] | data-length frame       | 0X04                   |
| Data[3] | command frame           | 0X03                   |
| Data[4] | Specify a single arm    | 0x01(Left)/0x02(Right) |
| Data[5] | Specify the servo motor | Joint_id    (1-7)      |
| Data[5] | end frame               | 0XFA                   |

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
| Data[5] | low  angle of No.1 steering gear   | Servo_Encoder_Low  |
| Data[6] | end frame                          | 0XFA               |

Example:

Assuming Atom has successfully connected：

Return value of port：FE FE 04 03 08 00 FA

---

### 设置零点

| Domain  | Explanation             | Data                   |
| :------ | :---------------------- | :--------------------- |
| Data[0] | identification frame    | 0XFE                   |
| Data[1] | identification frame    | 0XFE                   |
| Data[2] | data-length frame       | 0X04                   |
| Data[3] | command frame           | 0X04                   |
| Data[4] | Specify a single arm    | 0x01(Left)/0x02(Right) |
| Data[5] | Specify the servo motor | Joint_id    (1-7)      |
| Data[5] | end frame               | 0XFA                   |

Example:

Port transmission：FE FE 04 04 01 01 FA

no return value

---

### 设置LED灯的RGB值

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

no return value

---

