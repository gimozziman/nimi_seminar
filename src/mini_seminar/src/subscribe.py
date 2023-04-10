#!/usr/bin/env python
#-*- codfig: utf-8 -*-

import rospy
from std_msgs.msg import String

def  callback(data):
    print(data.data)

def subscribe():
    rospy.init_node('sub',anonymous=True)

    rospy.Subscriber('sewon_team', String, callback)

    rospy.spin()

if __name__ == '__main__':
    subscribe()
    