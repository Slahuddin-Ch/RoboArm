#!/usr/bin/env python
from pynput import keyboard
import rospy
from control_msgs.msg import GripperCommandActionGoal
from pynput.keyboard import Listener, Key
global pub

def on_press(key):
    print("\nPress J -> Gripper Closes")
    print("Press K -> Gripper Opens")
    if rospy.is_shutdown():
        exit()
    global pub
    publish_data = GripperCommandActionGoal()
    try:
        if(key.char == 'j'):
            print("robot closes")
            publish_data.goal.command.position = 0.8
            pub.publish(publish_data)
        if(key.char == 'k'):
            print("robot opens")
            publish_data.goal.command.position = 0.0
            pub.publish(publish_data)

    except:
        print("press j or k or press ctrl key to exit")
        if(key == keyboard.Key.ctrl):
            exit() 


if __name__ == '__main__':
    rospy.init_node('keyboard_teleop_gripper', anonymous=True)
    pub = rospy.Publisher('/gripper/gripper_cmd/goal', GripperCommandActionGoal, queue_size=10)
    print("Press J -> Gripper Closes")
    print("Press K -> Gripper Opens")
    with Listener(on_press=on_press) as listener:  # Setup the listener
        listener.join()  # Join the thread to the main thread