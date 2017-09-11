# Exercises

## Run the turtlesim node:
```
$ rosrun turtlesim turtlesim_node
```
If you don't have it, install it:
```
$ sudo apt-get install ros-indigo-turtlesim
```

## Exercise 1: Publish velocity commands
Create a node that publishes velocity commands to the *_turtlesim_node* for moving the turtle. Check into which topic you need to publish and how the message should be built. The commands should be taken from the terminal.

## Exercise 2: Pose control.
We will create a node responsible for moving the turtle to a specific *_x,y* pose. The node should follow this behavior:

1. Take the goal pose and a tolerance value from the terminal.
2. Once a goal pose is read, check the current pose to determine the velocity in the *_x* and *_y* axis (you can ignore the orientation).
3. Move the turtle until the current pose is within the tolerance value from the goal pose.
4. Stop the turtle and ask for a new pose.


