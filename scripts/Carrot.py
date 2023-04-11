#!/usr/bin/env python

import rospy
import tf
import math
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose

angle=0

def handle_turtle_carrot_pose(msg):
    angle=angle+2
    if angle == 360:
        angle=0
    x = 1*math.cos(angle*0.0174533)
    y = 1*math.sin(angle*0.0174533)
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0), quaternion_from_euler(0, 0, msg.theta), rospy.Time.now(), turtlename, "world")
    br.sendTransform((x, y, 0), quaternion_from_euler(0, 0, 0), rospy.Time.now(), "carrot", '~turtle_tf_name')

if __name__ == '__main__':
    rospy.init_node('tf_turtle-carrot')
    turtlename = rospy.get_param('~turtle_tf_name')
    rospy.Subscriber('input_pose',
                 Pose,
                 handle_turtle_carrot_pose)
    rospy.spin()