#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker2():
    pub = rospy.Publisher('/autonomy', String, queue_size=10)
    rospy.init_node('talker2', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "Fueled By Autonomy"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker2()
    except rospy.ROSInterruptException:
        pass
