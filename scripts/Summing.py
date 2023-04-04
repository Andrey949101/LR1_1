#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64MultiArray
from std_msgs.msg import Int64

def callback(msgP):
    msgS = Int64MultiArray()
    msgS=msgP.data
    result = msgS[0] + msgS[1] + msgS[2]
    pub = rospy.Publisher('chat_Summing', Int64, queue_size=10)
    pub.publish(result)
    rospy.loginfo("Summing send %d", result)



rospy.init_node('Summing')
rospy.Subscriber('chat_Polynomial', Int64MultiArray, callback, queue_size=10)
rospy.spin()