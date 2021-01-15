#!/usr/bin/env python
""" module docstring, yo! """
import sys
import rospy
import speech_recognition as sr

from std_msgs.msg import String

RECORDING = sr.Recognizer()


def talker():
    """ docsctring, yo! """
    speech_recognition_pub = rospy.Publisher('speech_recognition', String, queue_size=1)

    rospy.init_node('speech_recognizer', anonymous=True)

    rate = rospy.Rate(1)
    speech_recognized = ''
    while not rospy.is_shutdown():
        with sr.Microphone() as source:
            speech_is_recognized = True
            RECORDING.adjust_for_ambient_noise(source)
            print("Please Say something:")
            try:
                audio = RECORDING.listen(source, timeout=2)
                speech_recognized = RECORDING.recognize_google(audio)

            except sr.WaitTimeoutError as e:
                speech_is_recognized = False
                speech_recognized = ''
                print("Timed out..")

            except sr.UnknownValueError as e:
                speech_is_recognized = False
                print("I didn`t get it..")

        if speech_is_recognized:
            print("You said: \n" + speech_recognized)
            msg = String()
            msg.data = speech_recognized
            speech_recognition_pub.publish(msg)

        rate.sleep()


if __name__ == '__main__':
    MYARGV = rospy.myargv(argv=sys.argv)
    if len(MYARGV) > 1:
        print("args not cared.. ")
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
