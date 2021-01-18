#!/usr/bin/env python
""" module docstring, yo! """
import rospy
import rosservice
from std_msgs.msg import String


def callback(data):
    """ docsctring, yo! """
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    spoken = data.data

    if spoken == 'record':
        rosservice.call_service("record_ros", ['record'])
    elif spoken == 'stop':
        rosservice.call_service("record_ros", ['stop'])
    else:
        rospy.loginfo("Nothing interpreted..")


def listener():
    """ docsctring, yo! """
    rospy.init_node('speech_interpreter', anonymous=True)
    rospy.Subscriber('speech_recognition', String, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()
