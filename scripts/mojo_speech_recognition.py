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
    
    while not rospy.is_shutdown():
        with sr.Microphone() as source:
            RECORDING.adjust_for_ambient_noise(source)
            print("Please Say something:")
            audio = RECORDING.listen(source)

            try:
                speech_recognized = RECORDING.recognize_google(audio)
            except sr.UnknownValueError as e:
                print("I didn`t get it..")
        try:
            print("You said: \n" + speech_recognized)
        except Exception as e:
            print(e)

        msg = String()
        msg.data = speech_recognized
        speech_recognition_pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    MYARGV = rospy.myargv(argv=sys.argv)
    if len(MYARGV) > 1:
        print("args not cared: ", URL)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass