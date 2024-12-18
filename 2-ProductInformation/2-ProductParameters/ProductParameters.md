# 一、机器人参数说明--myArm M750

> 第一章中，我们探讨了产品的卖点及其设计理念，为您提供了对产品高层次理解的全景视角。现在，让我们进入第二章——机器人参数说明。这一章节将是您理解产品技术细节的关键。详细了解这些技术参数，不仅可以帮助您充分认识到我们产品的先进性和实用性，而且还能够确保您能够更有效地利用这些技术来满足您的具体需求。

---

# 1 产品规格参数
## 1.1 机器参数

<!-- <img src="../../resources/9-FilesDownload/2-serialproduct/image.png" width="800" height="auto" /> -->

|     规格    |      参数        |
|:--------------|:-----------------|
| 型号        | myArm  M750    |
|DOF           |	6+1       |
|水平伸展范围     |	750            |
|总跨度	         |	1500mm          |
|自重	        |	3.2kg           |
|电源规格       |		24V5A                |
|重复定位精度	|±1mm                  |
|精确度        |	5 - 8mm                |
|工作载荷	     |	额定500g，峰值1Kg      |
|舵机数量	   |8	                     |
|舵机类型	    |工业级高精度数字伺服电机     |
|旋转能力	    |+/- 180°	               |
|末端执行器	   |平行夹爪 ，可选摄像头适配       |
|USB 连接	   |Type-C	                   |
|Atom 末端	  |5*5 LED灯矩阵	            |
|通讯帧率	   |>50Hz	                   |


## 1.2 软件基本功能支持

| 功能/开发环境 | 使用情况 |
| :------------: | :--------: |
| 关节运动 | 支持 |
| 笛卡尔运动 | 支持 |
| 无线控制 | 支持 |
| 紧急停止 | 支持 |
| Windows      | 支持 |
| Linux        | 支持 |
| MAC          | 支持 |
| ROS        | 支持 |
| Python       | 支持 |
| myblockly    | 支持 |
| mystudio     | 支持 |
| 串口控制协议 | 支持 |
     


---

# 2 控制核心参数

![控制核心](../../resources/2-ProductInformation/2-ProductParameters/2.2-ControlCoreParameters/ControlCore.png)

## 2.1 主控制器规格表

| **指标** | **参数**                                                          |
| :------- | :---------------------------------------------------------------- |
| 主控制   | M5Stack-basic                                                     |
| 主控型号 | ESP32                                                             |
| CPU      | 240MHz 双核心。<br> 600 DMIPS、520KB SRAM。<br> Wi-Fi、双模式蓝牙 |
| 蓝牙     | 2.4G/5G                                                           |
| 无线     | 2.4G 3D Antenna                                                   |
| 输入     | IN1, IN2, IN3, IN4, IN5, IN6                                      |
| 输出     | OUT1, OUT2, OUT3, OUT4, OUT5, OUT6                                |

## 2.2 辅助控制器 1 规格表

| **指标**           | **参数**                                                        |
| :----------------- | :-------------------------------------------------------------- |
| 辅助控制           | Atom                                                            |
| 辅助控制型号       | ESP32                                                           |
| 辅助控制器核心参数 | 240MHz 双核。<br> 600 DMIPS，520KB SRAM。<br> Wi-Fi、双模式蓝牙 |
| 辅助控制器闪光灯   | 4MB                                                             |
| LCD 显示           | 2.0"@320\*240 ILI9342C IPS 面板，<br> 最大亮度 853nit           |
| C 型               | \*1                                                             |

## 2.3 辅助控制器 2 规格表

| **指标**           | **参数**                                                        |
| :----------------- | :-------------------------------------------------------------- |
| 辅助控制           | Pico                                                            |
| 辅助控制型号       | ESP32                                                           |
| 辅助控制器核心参数 | 240MHz 双核。<br> 600 DMIPS，520KB SRAM。Wi-Fi、<br> 双模式蓝牙 |
| 辅助控制器闪存     | 4MB                                                             |
| TypeC              | \*1                                                             |

---

# 3 结构尺寸参数

> ！本章以毫米为距离单位，以度为角度单位。

## 3.1 产品尺寸和工作空间

![产品尺寸](../../resources/2-ProductInformation/2-ProductParameters/2.3-StructuralSizeParameters/M750_05.jpg)

## 3.2 底座安装尺寸

- 底座需采用法兰安装，可使用 M6 螺丝固定在对应的固定底座上。
- 使用前请确认安装的底座可以承受 3 倍于机身重量的承载，以防止使用过程中因运动速度提升导致产品固定松动而引起产品损坏。

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.3-StructuralSizeParameters/base-D.jpg" width="800" height="auto" />

图 1 底座正视图

## 3.3 手臂末端

- 机械臂的末端可与乐高组件孔和螺纹孔兼容。

![手臂末端](../../resources/2-ProductInformation/2-ProductParameters/2.3-StructuralSizeParameters/M750_03.jpg)

## 3.4 产品展示

![产品展示](../../resources/2-ProductInformation/2-ProductParameters/2.3-StructuralSizeParameters/M750_00.jpg)

<!-- [PDF Views](<../../resources/2-ProductFeature/320%202022款技术图示(1).pdf>)  -->

## 3.5 3D 模型下载

[M750模型下载](https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_3d_files/myArm300/%E5%A4%96%E5%8F%91_myarm%20M750.STEP)

<!-- Download link: [https://download.elephantrobotics.com/Product_3d_files/myCobot_320_M5_2022v1.2_230708.STEP](https://download.elephantrobotics.com/Product_3d_files/myCobot_320_M5_2022v1.2_230708.STEP) -->

<!-- <iframe
    src=""
    width="100%"
    height="600px"
    allowfullscreen="true"
    webkitallowfullscreen="true"
    mozallowfullscreen="true"
    frameborder="0">
</iframe> -->

---

# 4 电气特性参数

## 4.1 底座电气接口概述

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.4-ElectricalCharacteristicsParameters/base-T.jpg " width="800" height="auto" />
图 1 底座正视图

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.4-ElectricalCharacteristicsParameters/base-L.jpg " width="800" height="auto" />
图 2 底座左侧

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.4-ElectricalCharacteristicsParameters/base-R.jpg " width="800" height="auto" />
图 3 底座右侧

| 序号 | 接口名称         | 定义       | 功能             | 备注                |
| :--- | :--------------- | :--------- | :--------------- | :------------------ |
| 1    | Type C           | 通信接口   | 与 PC 通信       | 开发使用            |
| 2    | 屏幕             | 显示       | 与按钮一起使用   |                     |
| 3    | 按键             | 按键 A     | 与显示屏一起使用 |                     |
| 4    |                  | 按键 B     |                  |                     |
| 5    |                  | 按键 C     |                  |                     |
| 6    | 开关             | 电源开关   | 控制输入电源通断 | 带灯（通电灯亮）    |
| 7    | DC/IO 接口       | GND        | GND              |                     |
|      |                  | IN6        | 数字输入信号 1~6 | 仅在 NPN 模式下输入 |
|      |                  | IN5        |                  |                     |
|      |                  | IN4        |                  |                     |
|      |                  | IN3        |                  |                     |
|      |                  | IN2        |                  |                     |
|      |                  | IN1        |                  |                     |
|      |                  | 24V        | DC24V            |                     |
| 8    | Type C           | 通信接口   | 与 PC 通信       | 开发使用            |
| 9    | 电源 DC 输入接口 | DC24V 输入 | DC24V 输入       |                     |
| 10   | DC/IO 接口       | 24V        | DC24V            |                     |
|      |                  | OUT1       | 数字输出信号 1~6 | 仅在 PNP 模式下输出 |
|      |                  | OUT2       |                  |                     |
|      |                  | OUT3       |                  |                     |
|      |                  | OUT4       |                  |                     |
|      |                  | OUT5       |                  |                     |
|      |                  | OUT6       |                  |                     |
|      |                  | GND        | GND              |                     |
| 11   | 急停接口         | STOP       | 急停电路接口     |                     |

#### 4.1.1 Type C ：C 型接口用于与个人电脑连接和通信，可供开发人员使用。

#### 4.1.2 屏幕 ：屏幕用于显示 myArm 的通信状态，并通过 2 英寸 IPS 屏幕校准机器人移动到起点。

#### 4.1.3 按键 A、按键 B 和按键 C 用于以协调的方式操作屏幕。

#### 4.1.4 电源开关 ：电源开关用于控制主电源输入。如果关闭，控制器也会断电。

#### 4.1.5 24V 输出 ：内置 DC24V，可供用户使用。

#### 4.1.6 数字输入/输出：包括 6 个数字输入信号和 6 个数字输出信号，用于与其他设备交互，并与其他设备一起构成自动化系统的重要组成部分。

数字输入/输出：包括 6 个数字输入信号和 6 个数字输出信号，用于与其他设备交互，并与其他设备一起构成自动化系统的重要组成部分。

需要注意的是，输出信号为 PNP 形式，输入信号为 NPN 形式。以下是外部接线图：


<img src="../../resources/2-ProductInformation/2-ProductParameters/2.4-ElectricalCharacteristicsParameters/NPN-Connect.png " width="400" height="auto" /><br>

> PNP 链接<br>

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.4-ElectricalCharacteristicsParameters/PNP-Connect.jpg " width="400" height="auto" /><br>

#### 4.1.7 电源直流输入接口：采用 KPPX-4P R7BFDC 电源插座。制造商提供的 24V 9.2A DC 电源适配器也可用于为 myCobot320 供电。

#### 4.1.8 急停电路端子与急停按钮盒相连，可用于控制机器人的急停。

> **注意**: 使用机器人时必须连接急停开关，并确保急停开关电路始终处于连接状态。

## 4.2 机械壁末端电气接口

#### 4.2.1 机械臂末端介绍

A. 机械臂末端侧面接口示意如图 2-1 所示：

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.4-ElectricalCharacteristicsParameters/Atom-T.jpg " width="400" height="auto" /><br>

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.4-ElectricalCharacteristicsParameters/Atom-D.jpg" width="400" height="auto" /><br>

图 2-1 机械臂末端

| 序号 | 接口名称         | 定义       | 功能             | 备注                |
| :--- | :--------------- | :--------- | :--------------- | :------------------ |
| 9   | 末端 IO 接口         | 末端工具IO接口   | 与外部设备交互     | 开发使用            |
| 10    | 末端 Grove 接口           |       |   |                     |
| 11   | Type C 接口        |    |可用于和 PC 端连接通讯，更新固件使用  |                     |
| 12   | 末端 Atom        | LED   | 用于 5X5 RGB LED（G27）显示和按键功能（G39）          |
| 13   | 舵机接口     | 连接舵机       | 连接外部设备舵机   |                     |

#### 4.2.2 末端接口说明

A. 如表 2-1 为末端 IO 口的定义。

| 标签名 | 信号名 | 功能                            | 备注 |
| ------ | ------ | ------------------------------- | ---- |
| 5V0    | 5V     | 5V 电源                         |      |
| GND    | GND    | 主板电源信号地                  |      |
| 3V3    | 3V3    | 3.3V 电源                       |      |
| G22    | G22    | 3.3V-OUT-PIN 输出/3.3V-INT 输入 |      |
| G19    | G19    | 3.3V-OUT-PIN 输出/3.3V-INT 输入 |      |
| G23    | G23    | 3.3V-OUT-PIN 输出/3.3V-INT 输入 |      |
| G33    | G33    | 3.3V-OUT-PIN 输出/3.3V-INT 输入 |      |

​ 表 2-1 末端 IO 口

B. 末端 Grove 接口：Grove 接口 4 定义如图 2-2 所示

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.4-ElectricalCharacteristicsParameters/Atom-Grove.png " width="400" height="auto" /><br>

> 图 2-2 末端 Grove 接口

C. Type C 接口：可用于和 PC 端连接通讯，更新固件使用。

D. Atom：用于 5X5 RGB LED（G27）显示和按键功能（G39）

E. 舵机接口：用于末端拓展夹爪时使用，当前支持配套的自适应夹爪使用。



# 5 笛卡尔坐标系

## 5.1 关节坐标系
关节坐标系是以机械臂各旋转关节为基准的坐标系，下图中的白色虚线表示各关节的旋转轴，红色箭头表示关节的旋转方向，q1~q6表示1~6关节坐标系。
<img src="../../resources/2-ProductInformation/2-ProductParameters/2.5-CartesianCoordinateSystem/关节坐标系.jpg " width="auto" height="auto" /><br>

## 5.2 基坐标系

基坐标系是固定在机械臂底部的坐标系，其原点和坐标轴方向在运动学算法建模时确定，一般情况原点定在底座的中心点。 

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.5-CartesianCoordinateSystem/基坐标系.jpg " width="auto" height="auto" /><br>

 ## 5.3 工具坐标系

工具坐标系是固定在机械臂末端的坐标系，其原点和坐标轴方向在运动学算法建模时确定，一般情况原点定在机械臂末端法兰盘的中心点。

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.5-CartesianCoordinateSystem/工具坐标系.jpg " width="auto" height="auto" /><br>

 ## 5.4 运动学模型
下图所示是机械臂的运动学模型，图示位置是算法模型上的零点
<img src="../../resources/2-ProductInformation/2-ProductParameters/2.5-CartesianCoordinateSystem/dh_model.jpg " width="auto" height="auto" /><br>
 
 ### 5.4.1 零位校准
在运动学模型中，实际的零点在2、3关节上存在一些偏置，考虑到校准的方便，用户使用零位校准时对齐刻度线即可，无需对齐模型上的实际零点。
<img src="../../resources/2-ProductInformation/2-ProductParameters/2.5-CartesianCoordinateSystem/零位校准.jpg " width="auto" height="auto" /><br>
 
 ### 5.4.2 MDH 参数
DH参数用于描述相邻连杆的相对关系：

- a_i：沿 x_i：从 z_i 到 z_i+1 的距离

- alpha_i：绕 x_i：从 z_i 到 z_i+1

- d_i: 表示沿 z_i 从 x_i-1 到 x_i 的距离

- θ_i：围绕 z_i：从 x_i-1 到 x_i 的角度

<!-- Here is an article to refer to
[https://blog.csdn.net/hitgavin/article/details/104442034](https://blog.csdn.net/hitgavin/article/details/104442034)  -->

 ### 5.4.3 MDH 参数列表 

| 关节 | theta   | d     | a_i-1 |alpha_i-1 | offset |
| :--- | :------ | :---- | :---  | :----    | :----- |
| 1    | theta_1 | 173.9 | 0     | 0        | 0      |
| 2    | theta_2 | 0     | 0     | -PI/2    | -PI/2  |
| 3    | theta_3 | 0     |308.315| 0        | 0      |
| 4    | theta_4 | 327.9 | 0     | -PI/2    | 0      |
| 5    | theta_5 | 0     | 0     | PI/2     | 0      |
| 6    | theta_6 | 207   | 0     | -PI/2    | PI     |


 ### 5.4.4 关节限位
| Joint | Min   | Max  |
| :---  | :---- | :----|
| 1     | -165  | 165  |
| 2     | -80   | 100  |
| 3     | -100  | 80   |
| 4     | -160  | 160  |
| 5     | -90   | 120  |
| 6     | -180  | 180  |



# 二、机器人参数说明--MyArm C650

> 第一章中，我们探讨了产品的卖点及其设计理念，为您提供了对产品高层次理解的全景视角。现在，让我们进入第二章——机器人参数说明。这一章节将是您理解产品技术细节的关键。详细了解这些技术参数，不仅可以帮助您充分认识到我们产品的先进性和实用性，而且还能够确保您能够更有效地利用这些技术来满足您的具体需求。

## 1.机器人规格参数

<!-- <img src="../../resources/9-FilesDownload/2-serialproduct/image.png" width="800" height="auto" /> -->

| 规格         | 参数                |
| :----------- | :------------------ |
| DOF          | 6+1                 |
| 水平伸展范围 | 650                 |
| 总跨度       | 1300mm              |
| 自重         | 1.8kg               |
| 电源规格     | 12V5A               |
| 重复定位精度 | ±1mm                |
| 精确度       | 5 - 8mm             |
| 工作载荷     | -                   |
| 舵机数量     | 8                   |
| 舵机类型     | 高精度数字伺服电机  |
| 旋转能力     | +/- 180°            |
| 末端执行器   | 双指遥控+双按钮控制 |
| USB 连接     | Type-C              |
| Atom 末端    | 5\*5 LED 灯矩阵     |
| 通讯帧率     | >50Hz               |


## 2.控制核心参数

### 主控制器规格表

| **指标** | **参数**                                                          |
| :------- | :---------------------------------------------------------------- |
| **主控制**   | M5Stack-basic                                                     |
| **主控型号** | ESP32                                                             |
| **CPU**      | 240MHz 双核心。<br> 600 DMIPS、520KB SRAM。<br> Wi-Fi、双模式蓝牙 |
| **蓝牙**     | 2.4G/5G                                                           |
| **无线**     | 2.4G 3D Antenna                                                   |
| **输入**     | 1, 2, 3, 5, 18, 19, 21, 22, 23, 25, 26, 35, 36                    |
| **输出**     | 同输入共用                                                        |
| **LCD 显示器**         | 2.0" @ 320*240 ILI9342C IPS panel, maximum brightness 853nit         |
| **实体按键**           | 

### 辅助控制器规格表


| **指标**           | **参数**                                                        |
| :----------------- | :-------------------------------------------------------------- |
| **辅助控制**            | Atom                                                            |
| **辅助控制型号**        | ESP32                                                           |
| **辅助控制器核心参数**  | 240MHz 双核。<br> 600 DMIPS，520KB SRAM。<br> Wi-Fi、双模式蓝牙 |
| **辅助控制器闪光灯**    | 4MB                                                             |
| **LED矩阵**         | 5*5 LED灯矩阵                                         |
| **LCD 显示**           | 2.0"@320\*240 ILI9342C IPS 面板，<br> 最大亮度 853nit           |
| **C 型**                | \*1                                                             |
| **辅控扩展IO**      | G19, G21, G22, G23, G25, G33                          |
|</center>


---

## 3.结构尺寸参数

> ！本章以毫米为距离单位，以度为角度单位。

### 产品尺寸和工作空间

<img src="../../../myArm_Controller_650_docs\resources\2-ProductInformation\2-ProductParameters\C650_00.jpg" width="800" height="auto" />

### 底座安装尺寸

- 底座需采用法兰安装，可使用 M6 螺丝固定在对应的固定底座上。
- 使用前请确认安装的底座可以承受 3 倍于机身重量的承载，以防止使用过程中因运动速度提升导致产品固定松动而引起产品损坏。

<img src="../../../myArm_Controller_650_docs\resources\2-ProductInformation\2-ProductParameters\base-D.png" width="800" height="auto" />

图 1 底座正视图

### 手臂末端

- 机械臂的末端可与乐高组件孔和螺纹孔兼容。

<img src="../../../myArm_Controller_650_docs\resources\2-ProductInformation\2-ProductParameters\C650_01.jpg" width="800" height="auto" />

### 产品展示

<img src="../../../myArm_Controller_650_docs\resources\2-ProductInformation\2-ProductParameters\C650_03.jpg" width="800" height="auto" />



<!-- [PDF Views](<../../resources/2-ProductFeature/320%202022款技术图示(1).pdf>) -->

### 3D 模型下载

[C650模型下载](https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_3d_files/myArm300/%E5%A4%96%E5%8F%91_myarm%20C650.STEP)



<!-- Download link: [https://download.elephantrobotics.com/Product_3d_files/myCobot_320_M5_2022v1.2_230708.STEP](https://download.elephantrobotics.com/Product_3d_files/myCobot_320_M5_2022v1.2_230708.STEP) -->

<!-- <iframe
    src=""
    width="100%"
    height="600px"
    allowfullscreen="true"
    webkitallowfullscreen="true"
    mozallowfullscreen="true"
    frameborder="0">
</iframe> -->

# 4.电气特性参数

## 底座电气接口概述

<img src="../../resources/2-ProductInformation/2-ProductParameters/底座正视图.jpg" 
width="800" height="auto" />  
图 4.1 底座正视图

<img src="../../resources/2-ProductInformation/2-ProductParameters//底座左视图.jpg" width="800" height="auto" />  
图 4.2 底座左视图

<img src="../../resources/2-ProductInformation/2-ProductParameters/底座右视图.jpg" width="800" height="auto" />  
图 4.3 底座右视图

| 序号 | 接口名称         | 定义       | 功能             | 备注                |
| :--- | :--------------- | :--------- | :--------------- | :------------------ |
|  1 |      功能接口组一      | I/O接口  |   GPIO引脚   |           |
| 2    | 屏幕             | 显示       | 与按钮一起使用   |                     |
| 3    | 按键             | 按键 A     | 与显示屏一起使用 |                     |
| 4    |                  | 按键 B     |                  |                     |
| 5    |                  | 按键 C     |                  |     |
 |6   |       功能接口组二        |  I/O接口  | GPIO引脚 |    |
|7    | 复位按钮            | 系统复位   | 使主控复位    | |
| 8   | Type C 接口        |    |可用于和 PC 端连接通讯，更新固件使用  |                     |
| 9  |  Grove 接口1           |       |   |                     |
|10   | 功能接口组三            |  I/O接口  |   GPIO引脚  | |
| 11  |   Grove 接口2   |    ||                     |
|   |   Grove 接口3   |    ||                     |
|12   |电源 DC 输入接口 | DC24V 输入 | DC24V 输入       |                     |



#### A.功能接口组一接口的定义如下表：
| 标签 | 类型         | 功能|     备注         |                 
| :--- | :--------------- | :--------- | :--------------- | 
|  18 |    I/O     |   GPIO18   |  在使用TF卡时不可用   |
|  19 |    I/O     |   GPIO19   |  在使用TF卡时不可用   | 
|  23 |    I/O     |   GPIO23   |  在使用TF卡时不可用   | 
|  22 |    I/O     |   GPIO22   |   |              
|  21 |    I/O     |   GPIO21   |   |   
|  GND|   P    |   GND  |   |   
|  3V3|    P    |   GPIO22   |   |   
|  5V |    P    |   DC 5V   |   |   

#### B.功能接口组二与功能组三各个接口定义一致，接口的定义如下表：
| 标签 | 类型         | 功能|     备注         |                 
| :--- | :--------------- | :--------- | :--------------- | 
|  3 |    I/O     |   GPIO3   |  在使用TypeC或Grover 3 时不可用   |
|  1 |    I/O     |   GPIO1   | 在使用TypeC或Grover 3 时不可用  | 
|  16 |    I/O     |   GPIO16   |  暂不支持  | 
|  17 |    I/O     |   GPIO17   |  暂不支持 |              
|  2 |    I/O     |   GPIO2   |   |   
|  5 |    I/O     |   GPIO5   |     |
|  25 |    I/O     |   GPIO25   | 暂不支持  | 
|  26 |    I/O     |   GPIO26   |  在使用 Grover 2 时不可用  | 
|  35 |    I/O     |   GPIO35   |  暂不支持 |              
|  36 |    I/O     |   GPIO36   | 在使用Grover 2 时不可用  |  
|  RST|  -    |  Controller reset  |  暂不支持 |   
|  BAT|  -    |  	BTTERY  |  暂不支持 | 
|  3V3|    P    |   GPIO22   |   |  
|  5V |    P    |   DC 5V   |   | 
|  GND|   P    |   GND  |   |   
 

> **注意**: I/O:该功能信号包含输入和输出组合。

#### C.Grover接口：Grover接口定义图如下：

<img src="../../resources/2-ProductInformation/2-ProductParameters/1.png" width="800" height="auto" />  
图 4.4 Grover接口1定义图

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.png" width="800" height="auto" />  
图 4.5 Grover接口2定义图


<img src="../../resources/2-ProductInformation/2-ProductParameters/2.png" width="800" height="auto" />  
图 4.6 Grover接口3定义图

#### D.屏幕 ：屏幕用于显示 myArm 的通信状态，并通过 2 英寸 IPS 屏幕校准机器人移动到起点。

#### E.按键 A、按键 B 和按键 C 用于以协调的方式操作屏幕。


#### F.复位按钮 ：用于主控系统复位

#### G.Type C ：C 型接口用于与个人电脑连接和通信，可供开发人员使用。



## 机械臂末端电气接口

#### 1.机械臂末端介绍

A. 机械臂末端侧面接口示意如图  所示：

<img src="../../resources/2-ProductInformation/2-ProductParameters/末端侧面接口.jpg" width="400" height="auto" /><br>

<img src="../../resources/2-ProductInformation/2-ProductParameters/末端正视图.jpg" width="400" height="auto" /><br>

图 2-1 机械臂末端

| 序号 | 接口名称         | 定义       | 功能             | 备注                |
| :--- | :--------------- | :--------- | :--------------- | :------------------ |
| 13   | 末端 Atom        | LED   | 用于 5X5 RGB LED（G27）显示和按键功能（G39）          | |
| 14   | Type C 接口        |    |可用于和 PC 端连接通讯，更新固件使用  |                     |
| 15    | 末端 Grove 接口           |       |   |  |
| 16  | 末端 IO 接口         | 末端工具IO接口   | 与外部设备交互     | 开发使用            |   
| 17  | 舵机接口     | 连接舵机       | 连接外部设备舵机   |                     |

#### 2.末端接口说明

A. 如表为末端 IO 口的定义。

| 标签名 | 信号名 | 功能                            | 备注 |
| ------ | ------ | ------------------------------- | ---- |
| 5V0    | 5V     | 5V 电源                         |      |
| GND    | GND    | 主板电源信号地                  |      |
| 3V3    | 3V3    | 3.3V 电源                       |      |
| G22    | G22    | 3.3V-OUT-PIN 输出/3.3V-INT 输入 |      |
| G19    | G19    | 3.3V-OUT-PIN 输出/3.3V-INT 输入 |      |
| G23    | G23    | 3.3V-OUT-PIN 输出/3.3V-INT 输入 |      |
| G33    | G33    | 3.3V-OUT-PIN 输出/3.3V-INT 输入 |      |


B. 末端 Grove 接口：Grove 接口 4 定义如图所示

<img src="../../resources/2-ProductInformation/2-ProductParameters/Atom-Grove.png" width="400" height="auto" /><br>

> 

C. Type C 接口：可用于和 PC 端连接通讯，更新固件使用。

D. Atom：用于 5X5 RGB LED（G27）显示和按键功能（G39）

E. 舵机接口：用于末端拓展夹爪时使用，当前支持配套的自适应夹爪使用。

---


# 5 笛卡尔坐标系

## 5.1 关节坐标系
关节坐标系是以机械臂各旋转关节为基准的坐标系，下图中的白色虚线表示各关节的旋转轴，红色箭头表示关节的旋转方向，q1~q6表示1~6关节坐标系。
<img src="../../resources/2-ProductInformation/2-ProductParameters/2.3-StructuralSizeParameters/关节坐标系.jpg" width="auto" height="auto" /><br>

## 5.2 基坐标系

基坐标系是固定在机械臂底部的坐标系，其原点和坐标轴方向在运动学算法建模时确定，一般情况原点定在底座的中心点。 

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.3-StructuralSizeParameters/基坐标系.jpg" width="auto" height="auto" /><br>

 ## 5.3 工具坐标系

工具坐标系是固定在机械臂末端的坐标系，其原点和坐标轴方向在运动学算法建模时确定，一般情况原点定在机械臂末端法兰盘的中心点。

<img src="../../resources/2-ProductInformation/2-ProductParameters/2.3-StructuralSizeParameters/工具坐标系.jpg" width="auto" height="auto" /><br>

 ## 5.4 运动学模型
下图所示是机械臂的运动学模型，图示位置是算法模型上的零点
<img src="../../resources/2-ProductInformation/2-ProductParameters/2.3-StructuralSizeParameters/dh_model.jpg" width="auto" height="auto" /><br>
 
 ### 5.4.1 零位校准
在运动学模型中，实际的零点在2、3关节上存在一些偏置，考虑到校准的方便，用户使用零位校准时对齐刻度线即可，无需对齐模型上的实际零点。
<img src="../../resources/2-ProductInformation/2-ProductParameters/2.3-StructuralSizeParameters/零位校准.jpg" width="auto" height="auto" /><br>

 


 ### 5.4.2 MDH 参数



DH参数用于描述相邻连杆的相对关系：

- a_i：沿 x_i：从 z_i 到 z_i+1 的距离

- alpha_i：绕 x_i：从 z_i 到 z_i+1

- d_i: 表示沿 z_i 从 x_i-1 到 x_i 的距离

- θ_i：围绕 z_i：从 x_i-1 到 x_i 的角度


 ### 5.4.3 MDH 参数列表 

 | 关节 | alpha_i-1 | a_i-1    | d     | theta   | offset |
| :--- | :---- | :--- | :---- | :------ | :----- |
| 1    | 0     | 0    | 154 | theta_1 | 0      |
| 2    | -PI/2  | 0    | 0     | theta_2 | -PI/2  |
| 3    | 0     | 308.3 | 0     | theta_3 | 0      |
| 4    | -PI/2     | 0 |327.9    | theta_4 | 0  |
| 5    | PI/2  | 0    | 0 | theta_5 | 0      |
| 6    | -PI/2 | 0    | 131.3  | theta_6 | PI      |

# 三、机器人参数说明--TRACER
<img src="../../resources/4-FunctionsAndApplications/6-SDKDevelopment/5.2-DevelopmentAndUseBasedOnROS1/1_download/tracer.jpg" width="auto" height="auto" /><br>
## 3.1 机器人尺寸参数

| 参数名称 | 参数值 |  
| :--- | :--- | 
| 机器人高度 | 685 |
| 机器人宽度 | 570 |
| 机器人长度 | 155 |
| 整备重量   | 28~30 | 
| 轴距 | 360 |
| 电池类型 | 锂电池 24V 15Ah | 
| 电池参数 | 直流⽆刷 | 
| 动⼒驱动电机 | 2 X 150W | 
| 驻⻋形式 | 伺服刹⻋/安全触边 | 
| 转向形式 | 差速转向 | 
| 驱动电机传感器 | 光电1024 | 
| 防护等级 | IP22 | 
| 最高速度（m/s） | 1.8 | 
| 最小转弯半径（mm） | 可原地转弯 | 
| 最大爬坡能力（°） | 8° |
| 离地间隙（mm） | 30 | 
| 最⼤续航时间（h） | 8 | 
| 最⼤⾏程(km) | 40km | 
| 充电时间（h） | 2h | 
| ⼯作温度（℃） | -10 ~ 40°C | 
| 控制模式 | 遥控控制/指令控制模式 | 
| 遥控器 | 2.4G/极限距离 200M | 
| 通讯接口 | CAN | 

### 具体参数可阅读
[用户手册](https://agilexsupport.yuque.com/staff-hso6mo/ttpor0/rto97he0o03b0rpm)


---

[← 上一章](../1-ProductIntroduction/1-ProductIntroduction.md) | [下一章 →](../../3-BasicSettings/3-UserInstructions/UserInstructions.md)




