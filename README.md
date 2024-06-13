# ROS Project: Control Layer Between Unity and Kinova Robotic Arm

## Project Overview

This project aims to create a control layer between a Unity VR project and the ROS drivers of a Kinova robotic arm. It mostly transforms a standard ROS message into a custom ROS message used by Kinova's drivers.

## Current Status

Unfortunately, I no longer have access to the Kinova robot with which this project was developed. As such, I cannot verify whether it is still functioning correctly.

## Installation Instructions

- **Operating System**: This project was developped using ROS Noetic on Ubuntu 20.04.
- **Kinova Robot**: The Kinova ROS drivers can be found [here](https://github.com/Kinovarobotics/ros_kortex).
- **Unity-ROS Bridge**: This can be found at the [Unity Robotics Hub](https://github.com/Unity-Technologies/Unity-Robotics-Hub) and is used to connect Unity to ROS. For tutorials and guidance on setting up ROS in Unity, including the ROS-TCP-Endpoint, follow their [ROS_setup tutorial](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/pick_and_place/0_ros_setup.md). ROS Noetic was used for this project. Note: you will need to change the first line of code of the file ROS-TCP-Endpoint/src/ros_tcp_endpoint/default_server_endpoint.py to
```bash
#!/usr/bin/env python3
```
This ensures that the Endpoint works with Python 3.

## Usage

To launch the control layer so that the Unity messages are transferred to the robot, you can run the command:
```bash
roslaunch unity_kinova kinova_real_time.launch
```
This command will start the Kinova ROS Kortex drivers, the ROS-TCP-Endpoint drivers, and the control layer node. For more information about the Kinova Kortex and its possible arguments, you can look at their [ReadMe page](https://github.com/Kinovarobotics/ros_kortex/blob/noetic-devel/kortex_driver/readme.md). Make sure to modify the host argument to the IP of your robot.

## Disclaimer

Due to the lack of access to the original hardware, this project may not work as expected. Please test it thoroughly in your environment and report any issues you encounter.
