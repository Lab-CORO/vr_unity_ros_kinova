#!/usr/bin/env python3

import rospy
import tf

from geometry_msgs.msg import Pose

# Global variables
pub = rospy.Publisher('/gen3/unity/tcp_tf_pose', Pose, queue_size=1)
counter = 0

def publish_pose(trans, rot):
    new_pose = Pose()
    new_pose.position.x = trans[0]
    new_pose.position.y = trans[1]
    new_pose.position.z = trans[2]
    new_pose.orientation.x = rot[0]
    new_pose.orientation.y = rot[1]
    new_pose.orientation.z = rot[2]
    new_pose.orientation.w = rot[3]

    global counter
    counter += 1

    if counter%5 == 0:
        rospy.loginfo(new_pose)
        pub.publish(new_pose)

def tf_listener():
    rospy.init_node('kinova_unity_tcp_tf_position')
    listener = tf.TransformListener()

    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform("/base_link","/tool_frame",rospy.Time(0))
            publish_pose(trans, rot)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
            

if __name__ == "__main__":
    try:
        tf_listener()
    except rospy.ROSInterruptException:
        pass