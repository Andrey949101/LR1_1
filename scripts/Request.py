#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_msgs.msg import Int64MultiArray

def callback(msg):
    rospy.loginfo("Request heard result %d", msg.data)

rospy.init_node('Request')
pub = rospy.Publisher('chat_Request', Int64MultiArray, queue_size=10)
rate = rospy.Rate(1)

def start_talker():
    msg = Int64MultiArray()
    msg1 = Int64()
    msg2 = Int64()
    msg3 = Int64()
    msg1 = int(input("Введите х: "))
    msg2 = int(input("Введите у: "))
    msg3 = int(input("Введите z: "))
    '''rospy.set_param('ros_x', msg1)
    rospy.set_param('ros_y', msg2)
    rospy.set_param('ros_z', msg3)'''
    msg.data = msg1,msg2,msg3
    print(msg)
    while not rospy.is_shutdown():
        pub.publish(msg)
        rospy.Subscriber('chat_Summing', Int64, callback, queue_size=10)
        rate.sleep()

try:
    start_talker()
    rospy.spin()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
