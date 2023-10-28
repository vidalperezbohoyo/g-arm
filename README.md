# G-Arm
This is the official repo of a full open source 3D printed robotic arm called G-Arm.

# How to make it?
1. Generate all the .stl files from the source files in FreeCAD. Then print them with the recommended densities shown here.
2. Buy all the necessary parts (or other equivalent) listed here.
3. Connect the electronics as this diagram.
4. Cross your fingers and install the software.

# Software to control it
1. Currently, it uses [**GRBL**](https://github.com/bdring/Grbl_Esp32) as the integrated firmware in the robot's base. The required GRBL configuration can be found here.
2. It is recommended to control it at a high level using ROS 2 and MoveIt2. For that, you have to install [**ROS 2 Humble**](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html) and [**MoveIt 2**](https://moveit.ros.org/install-moveit2/binary/). Also, you have to copy
the ROS 2 packages created for this robot into your ROS 2 workspace. On top of that, you have the [**PyMoveit API**](https://github.com/AndrejOrsula/pymoveit2) installed.
3. If you don't want to use via ROS 2, you can use the Python classes from this folder to control the robot at middle level.
