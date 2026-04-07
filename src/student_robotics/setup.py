from setuptools import find_packages, setup

package_name = 'student_robotics'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='christian.kissling@students.unibe.ch',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'circle_motion = student_robotics.circle_motion:main',
        ],
    },
)

Now build using the following aliases:
```bash
root@49ed0b86c179:/workspace/turtlebot3_ws# alias cb
alias cb='cd /workspace/turtlebot3_ws && colcon build --symlink-install --parallel-workers $(nproc)'
root@49ed0b86c179:/workspace/turtlebot3_ws# alias sb
alias sb='source /workspace/turtlebot3_ws/install/setup.bash'
root@49ed0b86c179:/workspace/turtlebot3_ws# 
```


```bash
root@49ed0b86c179:/workspace/turtlebot3_ws/src/student_robotics# cb
Starting >>> turtlebot3_msgs
Starting >>> dynamixel_sdk
Starting >>> turtlebot3_description                                                
Starting >>> dynamixel_sdk_custom_interfaces
Starting >>> turtlebot3_cartographer
Starting >>> turtlebot3_gazebo
Starting >>> turtlebot3_manipulation_gazebo
Starting >>> turtlebot3_navigation2
Finished <<< turtlebot3_cartographer [3.26s]                                                                           
Starting >>> turtlebot3_teleop
Finished <<< turtlebot3_description [5.16s]                                                            
Finished <<< turtlebot3_navigation2 [5.47s]                                                            
Starting >>> student_robotics
Finished <<< turtlebot3_teleop [10.0s]                                                                        
Finished <<< student_robotics [7.87s]                                                                         
Finished <<< dynamixel_sdk_custom_interfaces [13.9s]                                                          
Finished <<< turtlebot3_manipulation_gazebo [18.5s]                                                              
Finished <<< turtlebot3_msgs [19.3s]                                                                          
Starting >>> turtlebot3_example
Starting >>> turtlebot3_fake_node
Finished <<< turtlebot3_fake_node [4.09s]                                                                       
Finished <<< dynamixel_sdk [25.6s]                                                                              
Starting >>> turtlebot3_node
Starting >>> dynamixel_sdk_examples
Finished <<< turtlebot3_example [6.51s]                                                                      
Finished <<< turtlebot3_node [4.28s]                                                                                
Starting >>> turtlebot3_bringup
--- stderr: turtlebot3_gazebo                                                                                          
CMake Warning (dev) at /usr/share/cmake-3.22/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
  The package name passed to `find_package_handle_standard_args` (PkgConfig)
  does not match the name of the calling package (gazebo).  This can lead to
  problems in calling code that expects `find_package` result variables
  (e.g., `_FOUND`) to follow a certain pattern.
Call Stack (most recent call first):
  /usr/share/cmake-3.22/Modules/FindPkgConfig.cmake:99 (find_package_handle_standard_args)
  /usr/lib/x86_64-linux-gnu/cmake/gazebo/gazebo-config.cmake:72 (include)
  CMakeLists.txt:23 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.

---
Finished <<< turtlebot3_gazebo [35.5s]
Starting >>> turtlebot3_simulations
Finished <<< turtlebot3_bringup [5.95s]                                                                                 
Starting >>> turtlebot3
Finished <<< dynamixel_sdk_examples [10.8s]                                                                               
Finished <<< turtlebot3_simulations [1.44s]                                                                  
Finished <<< turtlebot3 [1.26s]                          

Summary: 17 packages finished [1min 32s]
  1 package had stderr output: turtlebot3_gazebo
root@49ed0b86c179:/workspace/turtlebot3_ws# 
root@49ed0b86c179:/workspace/turtlebot3_ws# sb
root@49ed0b86c179:/workspace/turtlebot3_ws# 
```
