# First steps in ROS

## Install ROS Indigo
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116
$ sudo apt-get update
$ sudo apt-get install ros-indigo-desktop-full
```

## Create the workspace
1. Create the workspace folders: 
```
$ mkdir catkin_ws
$ cd catkin_ws
$ mkdir src
``` 

2. Initialize the workspace:
```
$ cd src
$ catkin_init_workspace
```


## Build the workspace
1. While in the *_catkin_workspace* folder do:
```
$ catkin_make
```

This creates the following folder structure:
```
catkin_ws
    |-build
    |-devel
    |-src
```

2. Source the workspace:
```
$ source devel/setup.bash
```

**NOTE:** You will need to source your workspace on every terminal you open, to avoid this, we can source it permanently by:
```
$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```
Assuming your workspace is in your user's folder.

## Creating a node in python

1. Go to _src_ folder.
2. Create a package by:
```
$ catkin_create_pkg my_package
```
3. Go into the package directory and create a folder _nodes_ :
```
$ cd my_package
$ mkdir nodes
```
4. Create the python executable and make it executable:
```
$ cd nodes
$ touch my_package.py
$ chmod +x my_package.py
```
5. The file *_my_package.py* is ready for coding.


