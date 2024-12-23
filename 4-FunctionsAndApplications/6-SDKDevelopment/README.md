# SDK Development Guide

## 1. Operating Environment

The MyController S570 is a high-performance robotic controller. Although it does not have a built-in system, it supports multiple operating systems, including Windows and Linux. Therefore, it is essential to integrate the **exoskeleton** with the **operating system** during use. Please prepare the operating system before using the device.

## 2. Development Environment

In order to meet the diverse application needs of the robot in various scenarios, we have adapted the robot to multiple programming languages. So far, we have adapted the following mainstream programming languages, and we believe you can develop using any of the following languages. Please follow the instructions strictly. Any omitted steps may result in failure to run the corresponding language. We wish you a successful experience with the robot.

| **If you wish to use the following programming languages, please ensure that your robot is configured with USB/Wi-Fi mode in the responder section, and confirm that the connection is correct.** |
| :------------------------------------------------------------------------------------------------------------- |

- [6.1 Python](./5.1-BasedOnPythonDevelopmentAndUse/1_download.md)<br>
  Our robot supports Python, and the development of the Python API library is becoming more refined. The robot's joint angles, coordinates, gripper, and other aspects can be controlled through Python.<br>

- [6.2 ROS1](./5.2-DevelopmentAndUseBasedOnROS1/1_download.md)<br>
  ROS (Robot Operating System) is an open-source robot operating system that provides endless possibilities for robot development and control. Our robot can be controlled through ROS's rich control features and modular approach. Whether it's joint control, path planning, or perception feedback, ROS provides corresponding tools and libraries to make the control process more flexible and efficient.<br>

<!-- - [6.3 Communication](./5.4-DevelopmentBasedOnCommunicationProtocolPackage//5.4.1-CommunicationDoc.md)<br>
  If you have a certain understanding of information theory, encoding, and robot communication, you should understand that all communication stems from data transmission. To facilitate users in operating the robot, we have made available a communication protocol based on serial communication. You can use a serial port assistant or encapsulate it in any programming language you are familiar with to control the robot. -->

---

[← Previous Chapter](../5-BasicFunctions/5.1-Minirobot/README.md) | [Next Chapter →](../7-SuccessfulCases/7-SuccessfulCases.md)
