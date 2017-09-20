# Launch a Youbot simulation using Gazebo

## Install the controllers
```
$ sudo apt-get install ros-indigo-ros-control ros-indigo-ros-controllers ros-indigo-gazebo-ros-control
```

## Clone the simulation and description repositories

1. In the *src* folder of your workspace, execute:
```
$ git clone http://github.com/youbot/youbot_description.git -b indigo-devel
$ git clone http://github.com/youbot/youbot_simulation.git
```

2. Build the workspace. 

## Launch the simulator (base only)
```
$ roslaunch youbot_gazebo_robot youbot_base_only.launch 
```

