# Übungsblatt 06: ROS 2 Fundamentals: Topics, Nodes & Communication

[Link to repo](https://github.com/susifohn/lecture6-ros2demo/tree/main)

## Prerequisites
Following the readme went ok, but forgot to set the **GPU Passthrough**. Went through after the correction. 

Next the turtlebot house environment did not show up on *localhost:6080* just an empty world. After some desperate www search with no success, suddenly the house env did show up and the turtlebot was controllable.

![house](./assets/CPS_Ex06_turtlebot_house.png)

## Aufgabe 1a

Do the following steps

```bash
root@49ed0b86c179:/workspace/turtlebot3_ws# cd /workspace/turtlebot3_ws/src

root@49ed0b86c179:/workspace/turtlebot3_ws/src# ls -al
total 0
drwxr-xr-x 1 root root 4096 Apr  3 17:53 .
drwxrwxrwx 1 root root 4096 Apr  7 20:51 ..
drwxr-xr-x 1 root root 4096 Apr  3 17:54 DynamixelSDK
drwxr-xr-x 1 root root 4096 Apr  3 17:53 turtlebot3
drwxr-xr-x 1 root root 4096 Apr  3 17:53 turtlebot3_msgs
drwxr-xr-x 1 root root 4096 Apr  3 17:53 turtlebot3_simulations
root@49ed0b86c179:/workspace/turtlebot3_ws/src# 
root@49ed0b86c179:/workspace/turtlebot3_ws/src# ros2 pkg create --build-type ament_python student_robotics
going to create a new package
package name: student_robotics
destination directory: /workspace/turtlebot3_ws/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['root <christian.kissling@students.unibe.ch>']
licenses: ['TODO: License declaration']
build type: ament_python
dependencies: []
creating folder ./student_robotics
creating ./student_robotics/package.xml
creating source folder
creating folder ./student_robotics/student_robotics
creating ./student_robotics/setup.py
creating ./student_robotics/setup.cfg
creating folder ./student_robotics/resource
creating ./student_robotics/resource/student_robotics
creating ./student_robotics/student_robotics/__init__.py
creating folder ./student_robotics/test
creating ./student_robotics/test/test_copyright.py
creating ./student_robotics/test/test_flake8.py
creating ./student_robotics/test/test_pep257.py

[WARNING]: Unknown license 'TODO: License declaration'.  This has been set in the package.xml, but no LICENSE file has been created.
It is recommended to use one of the ament license identitifers:
Apache-2.0
BSL-1.0
BSD-2.0
BSD-2-Clause
BSD-3-Clause
GPL-3.0-only
LGPL-3.0-only
MIT
MIT-0
root@49ed0b86c179:/workspace/turtlebot3_ws/src# 
root@49ed0b86c179:/workspace/turtlebot3_ws/src# cd student_robotics/
root@49ed0b86c179:/workspace/turtlebot3_ws/src/student_robotics# ls -al
total 8
drwxr-xr-x 1 root root 4096 Apr  7 21:07 .
drwxr-xr-x 1 root root 4096 Apr  7 21:07 ..
-rw-r--r-- 1 root root  652 Apr  7 21:07 package.xml
drwxr-xr-x 1 root root 4096 Apr  7 21:07 resource
-rw-r--r-- 1 root root  101 Apr  7 21:07 setup.cfg
-rw-r--r-- 1 root root  723 Apr  7 21:07 setup.py
drwxr-xr-x 1 root root 4096 Apr  7 21:07 student_robotics
drwxr-xr-x 1 root root 4096 Apr  7 21:07 test
root@49ed0b86c179:/workspace/turtlebot3_ws/src/student_robotics# 
```

Next is to add to the *package.xml* the following

```xml
<depend>rclpy</depend>
<depend>geometry_msgs</depend>
<depend>nav_msgs</depend>
```
Then create *circle_motion.py*  in the *student_robotics/student_robotics" directory with content:

```python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleMotion(Node):
    def __init__(self):
        super().__init__('circle_motion')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz
        self.get_logger().info('CircleMotion node started')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.3   # m/s
        msg.angular.z = 0.5  # rad/s
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CircleMotion()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

Also make sure *setup.py* has the entry point registered:

```python
entry_points={
    'console_scripts': [
        'circle_motion = student_robotics.circle_motion:main',
    ],
},
```
