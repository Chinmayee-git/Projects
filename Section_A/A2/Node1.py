#!/usr/bin/env python3
# license removed for brevity

import rospy
from std_msgs.msg import String

def talker1():
    pub = rospy.Publisher('/team_abhiyaan', String, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        hello_str = "Team Abhiyaan: "
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker1()
    except rospy.ROSInterruptException:
        pass
