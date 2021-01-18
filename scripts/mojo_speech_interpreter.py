#!/usr/bin/env python
""" module docstring, yo! """
import rospy
import rosservice
from std_msgs.msg import String
from record_ros.srv import String_cmd


def callback(data):
    """ docsctring, yo! """
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)

    spoken = data.data
    
    
    if spoken == 'record':
	rospy.loginfo(rospy.get_caller_id() + " Rosbag record command.")
	CMD("record")
    elif spoken == 'stop':
	rospy.loginfo(rospy.get_caller_id() + " Rosbag stop command.")
	CMD("stop")
    else:
        rospy.loginfo(rospy.get_caller_id() + " Nothing interpreted..")


def listener():
    """ docsctring, yo! """
    rospy.init_node('speech_interpreter', anonymous=True)
    rospy.Subscriber('speech_recognition', String, callback)

    rospy.spin()


if __name__ == '__main__':
    print "Waiting for record ros service.."
    rospy.wait_for_service('/record/cmd')
    print "The wait is over."
    CMD = rospy.ServiceProxy('/record/cmd', String_cmd)
    listener()
