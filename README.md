# RoboArm

A ros based package with ur5 and a gripper

## Getting Started:

### Prerequisites:

- The build is only yet tested on ROS melodic but it may work on other distributions as well.

### Install:

- Make a local cakin workspace:
```
mkdir -p ~/catkin_ws/src
```
- Clone the repository to your workspace:
```
cd ~/catkin_ws/src
git clone git@github.com:Slahuddin-Ch/RoboArm.git
```

- Install project dependencies using rosdep:
```
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r -y
```
- Install all submodules:
```
cd ~/catkin_ws/src/{Workspace}
git submodule init
git submodule update --recursive
```

- Build and source the workspace:
```
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
```

### Launch:

- Launch robot simulation:
```
roslaunch icl_ur5_setup_gazebo icl_ur5_gripper.launch
```

- To check UR5 with moveit:
```
roslaunch icl_ur5_setup_moveit_config ur5_gripper_moveit_planning_execution.launch sim:=true
```

-  Rviz to visualize the trajectory
```
roslaunch icl_ur5_setup_moveit_config moveit_rviz.launch config:=true
```

Goto the planning group dropdown menu and choose gripper.

Goto the goal state and and choose CLOSE and then click on Plan and Execute.
