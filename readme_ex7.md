# Übungsblatt 07: Visualization ¬ SLAM

[Link to repo](https://github.com/susifohn/lecture6-ros2demo/tree/main)

Name: Christian.Kissling@students.unibe.ch

Ros2 version. local 5.1.3

## Prerequisites
I am using the pre installations of exercise 6. 
So I can use my windows PC and the already installed Docker Desktop. 

## Setup procedure

1. Start Docker Desktop, which is installed already
1. Run VS Code in my workspace folder of exercise 6 ```lecture6-ros2demo```
2. As then VS Code prompts, *run in container*
3. Close the terminal, by pressing a button, as prompted.
4. Then in the Terminal check using ```ros2 pkg list```
5. Some packages are missing, installing 
```bash
root@49ed0b86c179:/workspace/turtlebot3_ws# sudo apt update && sudo apt install -y   ros-humble-turtlebot3-cartographer   ros-humble-nav2-map-server
```

5. Check packages present:
```bash
root@49ed0b86c179:/workspace/turtlebot3_ws# ros2 pkg list | grep -E "cartographer|map_server"
cartographer_ros
cartographer_ros_msgs
nav2_map_server
turtlebot3_cartographer
root@49ed0b86c179:/workspace/turtlebot3_ws# 
```

5. Check "Burger"
```bash
root@49ed0b86c179:/workspace/turtlebot3_ws# env | grep TURT
TURTLEBOT3_MODEL=burger
root@49ed0b86c179:/workspace/turtlebot3_ws#
```

5. Run commands according *Übungsblatt 7* in separate terminals:
- ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
- ros2 launch turtlebot3_cartographer cartographer.launch.py - use_sim_time:=True
- ros2 run turtlebot3_teleop teleop_keyboard
- ros2 run nav2_map_server map_saver_cli -f ~/map


## Facing Problems
 1. There was no /workspace/turtlebot_ws
 2. The VNC server on localhost:6080 did show the directory listing with vnc-automation.html which then started the linux desktop. (The Password was 1234). Expected where the gazebo GUI. 

 **Solution**

 **Important** Stop containers in Docker Desktop!!

 In VS Code , press F1 and run ```Dev Containers: Rebuild Container```

 Then close the terminal, reopen a new one and enter ```pwd``` which shows ```/workspace/turtlebot3_ws```

 And ```echo $ROS_DISTRO``` shows ```humble```

 Enter ```tb3_world``` then localhost:6080 shows :

 ![gui gazebo](./assets/CPS_ex07_gazeboGUI.png)

 *Hint* CTLR+Shift+R does a hard refersh of the Browser, in case of errors like 


>Ein Fehler ist aufgetreten:
>
>Cannot read properties of null (reading 'addEventListener')
>TypeError: Cannot read properties of null (reading >'addEventListener')
>    at Object.addClipboardHandlers (http://localhost:6080/app/ui.>js:329:13)
>    at Object.start (http://localhost:6080/app/ui.js:101:12)
>    at http://localhost:6080/app/ui.js:47:27

 
## Check
```bash
root@e5e84fc1aa6b:/workspace/turtlebot3_ws# ros2 node list
/gazebo
/robot_state_publisher
/turtlebot3_diff_drive
/turtlebot3_imu
/turtlebot3_joint_state
/turtlebot3_laserscan
root@e5e84fc1aa6b:/workspace/turtlebot3_ws# 
```
Instead of 
- ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
 just run
 - tbs_world

 Now continue with 
 - ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True

 This starts **Rviz**

 ![Rviz](./assets/CPS_ex07_rviz.png)

 ## Now start SLAM

 1. ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True

 2. ros2 run turtlebot3_teleop teleop_keyboard

 Now we see the bot turning and moving according the teleop command. 

 See the video [video teleop.mp4](./assets/teleop.mp4)

 And moving arround on the map: [moving arround](./assets/explore.mp4)

 3. Save the map using again a new Terminal ```ros2 run nav2_map_server map_saver_cli -f ~/map```

now we have 
- ~map.yaml
- ~map.pgm

See the directory listing  below:

```bash
root@e5e84fc1aa6b:~# ll -h  | grep map
-rw-r--r-- 1 root root    0 May  3 08:06 .Xmodmap
-rw-r--r-- 1 root root  15K May  3 18:57 map.pgm
-rw-r--r-- 1 root root  121 May  3 18:57 map.yaml
drwxr-xr-x 2 root root 4.0K May  3 18:15 maps/
root@e5e84fc1aa6b:~# 
```

### What is going on
- The robot publishes laser scans (/scan)
- SLAM estimates position + environment simultaneously
- RViz visualizes the map (/map)
- Revisiting areas improves accuracy






