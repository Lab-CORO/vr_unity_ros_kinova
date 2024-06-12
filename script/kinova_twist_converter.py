#!/usr/bin/env python3

import rospy
from kortex_driver.msg import TwistCommand
from geometry_msgs.msg import Twist

'''
This script change a Twist.msg from geometry_msgs to the Kinova
TwistCommand.msg
'''

# Global publisher
pub = rospy.Publisher('/my_gen3/in/cartesian_velocity', TwistCommand, queue_size=1)

def callback(msg):
    '''
    Convert standard twist to Kinova twist message
    '''
    new_twist = TwistCommand()
    new_twist.reference_frame = 0
    new_twist.duration = 0

    new_twist.twist.linear_x = msg.linear.x
    new_twist.twist.linear_y = msg.linear.y
    new_twist.twist.linear_z = msg.linear.z

    new_twist.twist.angular_x = msg.angular.x
    new_twist.twist.angular_y = msg.angular.y
    new_twist.twist.angular_z = msg.angular.z

    rospy.loginfo(new_twist)

    pub.publish(new_twist)

def convert_twist_msg():
    '''
    Create the node and listen to a topic to get a Twist message.
    '''

    rospy.init_node('unity_kinova_twist_converter')
    rospy.Subscriber('/unity/kinova/twist', Twist, callback, queue_size=1)
    rospy.spin()

if __name__ == "__main__":
    try:
        convert_twist_msg()
    except rospy.ROSInterruptException:
        pass