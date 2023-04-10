#!/usr/bin/env python
#-*- codfig: utf-8 -*-

import rospy
from std_msgs.msg import String

def publish():
    rospy.init_node("pub",anonymous=True)
    name = rospy.Publisher('sewon_team', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        team_name = ["김민겸","김재현","정민규","문호형","노윤석","정재민","한규연","king윤세원"]
        for i in team_name:
            name.publish(i)
            print(i)
    rate.sleep()

 
if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass    