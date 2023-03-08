#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker_chisla')
pub1 = rospy.Publisher('Chisla_do_100', String, queue_size=10)
pub2 = rospy.Publisher('Sotni', String, queue_size=10)
rate = rospy.Rate(1)


def start_talker():
    msg = String()
    chisla = 0
    sotni = 1
    while not rospy.is_shutdown():
        hello_str_1 = str(chisla) 
        hello_str_2 = str(sotni) 

        if chisla<100:
            msg.data = hello_str_1
            pub1.publish(msg)
            rospy.loginfo(hello_str_1)
            chisla=chisla+10
        else: 
            msg.data = hello_str_2
            pub2.publish(msg)
            rospy.loginfo(hello_str_2)
            sotni=sotni+1
            chisla=0


        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')