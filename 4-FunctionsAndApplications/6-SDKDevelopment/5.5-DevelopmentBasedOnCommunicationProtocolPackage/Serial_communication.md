# 通信和信息命令

> **注意：** 在通过通信协议直接通信之前，需要在 BASIC 上烧录外骨骼的最新固件,并且烧录最新的 ATOM 固件

| **请详细阅读接口协议文档，并在测试后继续程序开发。** |
| :--------------------------------------------------- |

## 1 USB 通信设置

**_确保准备好以下设置：_**

- 主线接口：USB Type-C 连接电脑和 BASIC
- 波特率: 1000000
- 数据位: 8
- 奇偶校验位: none
- 停止位: 1

## 2 指令帧简介 & 指导

PC 通过 BASIC 传输数据,机械臂内部将数据解码为带有返回值的命令并使用串口通信协议在 5 毫秒内通过 BASIC 将结果发送回 PC,通信频率可达 200Hz

## 3 信息命令的发送和接收格式

发送和接收都应以十六进制表示。每条命令应包含 5 个部分，如下所示。第 3 和第 4 部分可以留空。

- 1 命令引脚：0xFE 0xFE
  - 不变
  - 不可或缺
- 2 有效长度:
  - 总长度包括针脚、序列号、功能代码和端点
  - 不可或缺
- 3 序列号：00 ~ 8F
  - 已开发指令的相应数量
  - 可以留空。
- 4 功能代码
  - 以目标为导向
  - 可以留空。
- 5 结束： 0XFA
  - 不变
  - 不可或缺

## 4 命令解释

| **类型** | **数据**   | **长度** | **功能**                     |
| :------- | :--------- | :------- | :--------------------------- |
| 指令框架 | 开始位： 0 | 1        | 起始帧识别，0XFE             |
|          | 开始位： 1 | 1        | 起始帧识别，0XFE             |
|          | 位数据长度 | 1        | 不同的命令对应不同的数据长度 |
|          | 指令位     | 1        | 取决于不同的命令             |
| 指令框架 | 数据       | 0-16     | 命令与数据，取决于不同的命令 |
| 结束框架 | 结束位     | 1        | 停止位，0XFA                 |

## 5 单一指令命令说明

### 读取双臂所有数据

| **数据域** | **说明**   | **数据** |
| :--------- | :--------- | :------- |
| Data[0]    | 识别帧     | 0XFE     |
| Data[1]    | 识别帧     | 0XFE     |
| Data[2]    | 数据长度帧 | 0X02     |
| Data[3]    | 指令帧     | 0X01     |
| Data[4]    | 结束帧     | 0XFA     |

示例:

串口传输：FE FE 02 01 FA

返回值：数据结构

| **数据域** | **说明**                 | **数据**                                                    |
| :--------- | :----------------------- | :---------------------------------------------------------- |
| Data[0]    | 返回值：识别帧           | 0XFE                                                        |
| Data[1]    | 返回值：识别帧           | 0XFE                                                        |
| Data[2]    | 返回值：返回长度         | 0X3C                                                        |
| Data[3]    | 返回值：命令帧           | 0X01                                                        |
| Data[4]    | 返回值: 左臂关节 1 高位  | Left_Servo1_high                                            |
| Data[5]    | 返回值: 左臂关节 1 低位  | Left_Servo1_Low                                             |
| Data[6]    | 返回值: 左臂关节 2 高位  | Left_Servo2_high                                            |
| Data[7]    | 返回值: 左臂关节 2 低位  | Left_Servo2_Low                                             |
| Data[8]    | 返回值: 左臂关节 3 高位  | Left_Servo3_high                                            |
| Data[9]    | 返回值: 左臂关节 3 低位  | Left_Servo3_Low                                             |
| Data[10]   | 返回值: 左臂关节 4 高位  | Left_Servo4_high                                            |
| Data[11]   | 返回值: 左臂关节 4 低位  | Left_Servo4_Low                                             |
| Data[12]   | 返回值: 左臂关节 5 高位  | Left_Servo5_high                                            |
| Data[13]   | 返回值: 左臂关节 5 低位  | Left_Servo5_Low                                             |
| Data[14]   | 返回值: 左臂关节 6 高位  | Left_Servo6_high                                            |
| Data[15]   | 返回值: 左臂关节 6 低位  | Left_Servo6_Low                                             |
| Data[16]   | 返回值: 左臂关节 7 高位  | Left_Servo7_High                                            |
| Data[17]   | 返回值: 左臂关节 7 低位  | Left_Servo7_Low                                             |
| Data[18]   | 返回值: 左臂遥感按钮状态 | Left_button_status (bit1:遥感按钮 bit2:按钮 1 bit3:按钮 2)  |
| Data[19]   | 返回值: 左臂遥感 x 值    | Left_remote_sensing_x-value                                 |
| Data[20]   | 返回值: 左臂遥感 y 值    | Left_remote_sensing_y-value                                 |
| Data[21]   | 返回值: 右臂关节 1 高位  | Right_Servo1_high                                           |
| Data[22]   | 返回值: 右臂关节 1 低位  | Right_Servo1_Low                                            |
| Data[23]   | 返回值: 右臂关节 2 高位  | Right_Servo2_high                                           |
| Data[24]   | 返回值: 右臂关节 2 低位  | Right_Servo2_Low                                            |
| Data[25]   | 返回值: 右臂关节 3 高位  | Right_Servo3_high                                           |
| Data[26]   | 返回值: 右臂关节 3 低位  | Right_Servo3_Low                                            |
| Data[27]   | 返回值: 右臂关节 4 高位  | Right_Servo4_high                                           |
| Data[28]   | 返回值: 右臂关节 4 低位  | Right_Servo4_Low                                            |
| Data[29]   | 返回值: 右臂关节 5 高位  | Right_Servo5_high                                           |
| Data[30]   | 返回值: 右臂关节 5 低位  | Right_Servo5_Low                                            |
| Data[31]   | 返回值: 右臂关节 6 高位  | Right_Servo6_high                                           |
| Data[32]   | 返回值: 右臂关节 6 低位  | Right_Servo6_Low                                            |
| Data[33]   | 返回值: 右臂关节 7 高位  | Right_Servo7_High                                           |
| Data[34]   | 返回值: 右臂关节 7 低位  | Right_Servo7_Low                                            |
| Data[35]   | 返回值: 右臂遥感按钮状态 | Right_button_status (bit1:遥感按钮 bit2:按钮 1 bit3:按钮 2) |
| Data[36]   | 返回值: 右臂遥感 x 值    | Right_remote_sensing_x-value                                |
| Data[37]   | 返回值: 右臂遥感 y 值    | Right_remote_sensing_y-value                                |
| Data[38]   | 返回值: 左臂 x 轴高位    | Right_Servo2_high                                           |
| Data[39]   | 返回值: 左臂 x 轴低位    | Right_Servo2_Low                                            |
| Data[40]   | 返回值: 左臂 y 轴高位    | Right_Servo3_high                                           |
| Data[41]   | 返回值: 左臂 y 轴低位    | Right_Servo3_Low                                            |
| Data[42]   | 返回值: 左臂 z 轴高位    | Right_Servo4_high                                           |
| Data[43]   | 返回值: 左臂 z 轴低位    | Right_Servo4_Low                                            |
| Data[44]   | 返回值: 左臂 rx 旋转高位 | Right_Servo5_high                                           |
| Data[45]   | 返回值: 左臂 rx 旋转低位 | Right_Servo5_Low                                            |
| Data[46]   | 返回值: 左臂 ry 旋转高位 | Right_Servo6_high                                           |
| Data[47]   | 返回值: 左臂 ry 旋转低位 | Right_Servo6_Low                                            |
| Data[48]   | 返回值: 左臂 rz 旋转高位 | Right_Servo7_High                                           |
| Data[49]   | 返回值: 左臂 rz 旋转低位 | Right_Servo7_Low                                            |
| Data[50]   | 返回值: 右臂 x 轴高位    | Right_Servo2_high                                           |
| Data[51]   | 返回值: 右臂 x 轴低位    | Right_Servo2_Low                                            |
| Data[52]   | 返回值: 右臂 y 轴高位    | Right_Servo3_high                                           |
| Data[53]   | 返回值: 右臂 y 轴低位    | Right_Servo3_Low                                            |
| Data[54]   | 返回值: 右臂 z 轴高位    | Right_Servo4_high                                           |
| Data[55]   | 返回值: 右臂 z 轴低位    | Right_Servo4_Low                                            |
| Data[56]   | 返回值: 右臂 rx 旋转高位 | Right_Servo5_high                                           |
| Data[57]   | 返回值: 右臂 rx 旋转低位 | Right_Servo5_Low                                            |
| Data[58]   | 返回值: 右臂 ry 旋转高位 | Right_Servo6_high                                           |
| Data[59]   | 返回值: 右臂 ry 旋转低位 | Right_Servo6_Low                                            |
| Data[60]   | 返回值: 右臂 rz 旋转高位 | Right_Servo7_High                                           |
| Data[61]   | 返回值: 右臂 rz 旋转低位 | Right_Servo7_Low                                            |
| Data[62]   | 结束符                   | 0XFA                                                        |

示例:

端口返回：FE FE 24 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FA

---

### 读取单臂所有数据

| **数据域** | **说明**   | **数据**          |
| :--------- | :--------- | :---------------- |
| Data[0]    | 识别帧     | 0XFE              |
| Data[1]    | 识别帧     | 0XFE              |
| Data[2]    | 数据长度帧 | 0X03              |
| Data[3]    | 指令帧     | 0X02              |
| Data[4]    | 指定单臂   | 0x01(左)/0x02(右) |
| Data[5]    | 结束帧     | 0XFA              |

示例:

串口传输：FE FE 03 02 01 FA

返回值：数据结构

| **数据域** | **说明**                 | **数据**                                                   |
| :--------- | :----------------------- | :--------------------------------------------------------- |
| Data[0]    | 返回值：识别帧           | 0XFE                                                       |
| Data[1]    | 返回值：识别帧           | 0XFE                                                       |
| Data[2]    | 返回值：返回长度         | 0X13                                                       |
| Data[3]    | 返回值：命令帧           | 0X02                                                       |
| Data[4]    | 返回值: 左臂关节 1 高位  | Left_Servo1_high                                           |
| Data[5]    | 返回值: 左臂关节 1 低位  | Left_Servo1_Low                                            |
| Data[6]    | 返回值: 左臂关节 2 高位  | Left_Servo2_high                                           |
| Data[7]    | 返回值: 左臂关节 2 低位  | Left_Servo2_Low                                            |
| Data[8]    | 返回值: 左臂关节 3 高位  | Left_Servo3_high                                           |
| Data[9]    | 返回值: 左臂关节 3 低位  | Left_Servo3_Low                                            |
| Data[10]   | 返回值: 左臂关节 4 高位  | Left_Servo4_high                                           |
| Data[11]   | 返回值: 左臂关节 4 低位  | Left_Servo4_Low                                            |
| Data[12]   | 返回值: 左臂关节 5 高位  | Left_Servo5_high                                           |
| Data[13]   | 返回值: 左臂关节 5 低位  | Left_Servo5_Low                                            |
| Data[14]   | 返回值: 左臂关节 6 高位  | Left_Servo6_high                                           |
| Data[15]   | 返回值: 左臂关节 6 低位  | Left_Servo6_Low                                            |
| Data[16]   | 返回值: 左臂关节 7 高位  | Left_Servo7_High                                           |
| Data[17]   | 返回值: 左臂关节 7 低位  | Left_Servo7_Low                                            |
| Data[18]   | 返回值: 左臂遥感按钮状态 | Left_button_status (bit1:遥感按钮 bit2:按钮 1 bit3:按钮 2) |
| Data[19]   | 返回值: 左臂遥感 x 值    | Left_remote_sensing_x-value                                |
| Data[20]   | 返回值: 左臂遥感 y 值    | Left_remote_sensing_y-value                                |
| Data[21]   | 返回值: 左臂 x 轴高位    | Right_Servo2_high                                          |
| Data[22]   | 返回值: 左臂 x 轴低位    | Right_Servo2_Low                                           |
| Data[23]   | 返回值: 左臂 y 轴高位    | Right_Servo3_high                                          |
| Data[24]   | 返回值: 左臂 y 轴低位    | Right_Servo3_Low                                           |
| Data[25]   | 返回值: 左臂 z 轴高位    | Right_Servo4_high                                          |
| Data[26]   | 返回值: 左臂 z 轴低位    | Right_Servo4_Low                                           |
| Data[27]   | 返回值: 左臂 rx 旋转高位 | Right_Servo5_high                                          |
| Data[28]   | 返回值: 左臂 rx 旋转低位 | Right_Servo5_Low                                           |
| Data[29]   | 返回值: 左臂 ry 旋转高位 | Right_Servo6_high                                          |
| Data[30]   | 返回值: 左臂 ry 旋转低位 | Right_Servo6_Low                                           |
| Data[31]   | 返回值: 左臂 rz 旋转高位 | Right_Servo7_High                                          |
| Data[32]   | 返回值: 左臂 rz 旋转低位 | Right_Servo7_Low                                           |
| Data[33]   | 结束帧                   | 0XFA                                                       |

示例:

端口返回：FE FE 13 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 14 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FA

---

### 读单臂单个编码器数据

| **数据域** | **说明**   | **数据**          |
| :--------- | :--------- | :---------------- |
| Data[0]    | 识别帧     | 0XFE              |
| Data[1]    | 识别帧     | 0XFE              |
| Data[2]    | 数据长度帧 | 0X04              |
| Data[3]    | 指令帧     | 0X03              |
| Data[4]    | 指定单臂   | 0x01(左)/0x02(右) |
| Data[5]    | 指定舵机   | Joint_id (1-7)    |
| Data[6]    | 结束帧     | 0XFA              |

示例:

串口传输：FE FE 04 03 01 01 FA

返回值：数据结构

| **数据域** | **说明**               | **数据**           |
| :--------- | :--------------------- | :----------------- |
| Data[0]    | 返回值：识别帧         | 0XFE               |
| Data[1]    | 返回值：识别帧         | 0XFE               |
| Data[2]    | 返回值：返回长度       | 0X04               |
| Data[3]    | 返回值：命令帧         | 0X03               |
| Data[4]    | 返回值: 关节编码值高位 | Servo_Encoder_High |
| Data[5]    | 返回值: 关节编码值低位 | Servo_Encoder_Low  |
| Data[6]    | 结束符                 | 0XFA               |

示例:

端口返回：FE FE 04 03 08 00 FA

---

### 设置零点

| **数据域** | **说明**   | **数据**          |
| :--------- | :--------- | :---------------- |
| Data[0]    | 识别帧     | 0XFE              |
| Data[1]    | 识别帧     | 0XFE              |
| Data[2]    | 数据长度帧 | 0X04              |
| Data[3]    | 指令帧     | 0X04              |
| Data[4]    | 指定单臂   | 0x01(左)/0x02(右) |
| Data[5]    | 指定舵机   | Joint_id (1-7)    |
| Data[6]    | 结束帧     | 0XFA              |

示例:

串口传输：FE FE 04 04 01 01 FA

返回值：数据结构

| **数据域** | **说明**         | **数据** |
| :--------- | :--------------- | :------- |
| Data[0]    | 返回值：识别帧   | 0XFE     |
| Data[1]    | 返回值：识别帧   | 0XFE     |
| Data[2]    | 返回值：返回长度 | 0X03     |
| Data[3]    | 返回值：命令帧   | 0X04     |
| Data[4]    | 返回值: 1        | 1        |
| Data[5]    | 结束符           | 0XFA     |

示例:

端口返回：FE FE 03 04 01 FA

---

### 设置 LED 灯的 RGB 值

| **数据域** | **说明**   | **数据**          |
| :--------- | :--------- | :---------------- |
| Data[0]    | 识别帧     | 0XFE              |
| Data[1]    | 识别帧     | 0XFE              |
| Data[2]    | 数据长度帧 | 0X06              |
| Data[3]    | 指令帧     | 0X05              |
| Data[4]    | 指令帧     | 0x01(左)/0x02(右) |
| Data[5]    | 红色数值   | R_Value           |
| Data[6]    | 绿色数值   | G_Value           |
| Data[7]    | 蓝色数值   | B_Value           |
| Data[8]    | 结束帧     | 0XFA              |

示例:

串口传输：FE FE 06 05 00 FF 00 FA

返回值：数据结构

| **数据域** | **说明**         | **数据** |
| :--------- | :--------------- | :------- |
| Data[0]    | 返回值：识别帧   | 0XFE     |
| Data[1]    | 返回值：识别帧   | 0XFE     |
| Data[2]    | 返回值：返回长度 | 0X03     |
| Data[3]    | 返回值：命令帧   | 0X05     |
| Data[4]    | 返回值: 1        | 1        |
| Data[5]    | 结束符           | 0XFA     |

示例:

端口返回：FE FE 03 05 01 FA

### 读取 basic 固件版本号

| **数据域** | **说明**   | **数据** |
| :--------- | :--------- | :------- |
| Data[0]    | 识别帧     | 0XFE     |
| Data[1]    | 识别帧     | 0XFE     |
| Data[2]    | 数据长度帧 | 0X02     |
| Data[3]    | 指令帧     | 0X06     |
| Data[4]    | 结束帧     | 0XFA     |

示例:

串口传输：FE FE 02 06 FA

返回值：数据结构

| **数据域** | **说明**               | **数据** |
| :--------- | :--------------------- | :------- |
| Data[0]    | 返回值：识别帧         | 0XFE     |
| Data[1]    | 返回值：识别帧         | 0XFE     |
| Data[2]    | 返回值：返回长度       | 0X03     |
| Data[3]    | 返回值：命令帧         | 0X06     |
| Data[4]    | 返回值: 固件版本号\*10 | 0x0C     |
| Data[5]    | 结束符                 | 0XFA     |

示例:

端口返回：FE FE 03 06 0C FA

### 读取 atom 固件版本号

| **数据域** | **说明**   | **数据**          |
| :--------- | :--------- | :---------------- |
| Data[0]    | 识别帧     | 0XFE              |
| Data[1]    | 识别帧     | 0XFE              |
| Data[2]    | 数据长度帧 | 0X02              |
| Data[3]    | 指令帧     | 0X07              |
| Data[4]    | 指令帧     | 0x01(左)/0x02(右) |
| Data[5]    | 结束帧     | 0XFA              |

示例:

串口传输：FE FE 02 07 01 FA

返回值：数据结构

| **数据域** | **说明**               | **数据**          |
| :--------- | :--------------------- | :---------------- |
| Data[0]    | 返回值：识别帧         | 0XFE              |
| Data[1]    | 返回值：识别帧         | 0XFE              |
| Data[2]    | 返回值：返回长度       | 0X03              |
| Data[3]    | 返回值：命令帧         | 0X06              |
| Data[4]    | 指令帧                 | 0x01(左)/0x02(右) |
| Data[5]    | 返回值: 固件版本号\*10 | 0x0C              |
| Data[6]    | 结束符                 | 0XFA              |

示例:

端口返回：FE FE 04 07 01 0C FA
