#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64
from std_msgs.msg import Int64MultiArray

pub = rospy.Publisher('chat_Polynomial', Int64MultiArray, queue_size=10)

def callback(msg):
    
    rospy.loginfo("Polynomial heard x %d; y %d; z %d", msg.data[0], msg.data[1], msg.data[2])
    msg = msg.data
    msgP = Int64MultiArray()
    msgP1 = Int64()
    msgP2 = Int64()
    msgP3 = Int64()
    msgP1 = msg[0]**1
    msgP2 = msg[1]**2
    msgP3 = msg[2]**3
    msgP.data = msgP1,msgP2,msgP3
    print(msgP)
    while not rospy.is_shutdown():
        rospy.loginfo("Polynomial send %d, %d, %d", msgP.data[0], msgP.data[1], msgP.data[2])
        pub.publish(msgP)
        rate.sleep()

rospy.init_node('Polynomial')
rate = rospy.Rate(10)
rospy.Subscriber('chat_Request', Int64MultiArray, callback, queue_size=10)
rospy.spin()

