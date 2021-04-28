#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

l = ['', '']

def callback1(data):
    global l
    l[0] = data.data

def callback2(data):
    global l
    l[1] = data.data
    rospy.loginfo(l[0] + l[1])

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/team_abhiyaan', String, callback1)
    rospy.Subscriber("/autonomy", String, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
