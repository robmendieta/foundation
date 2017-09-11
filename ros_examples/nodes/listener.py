#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String

class Listener:
	def __init__ (self):
		# Init node
		rospy.init_node("listener")
		rospy.loginfo("Listener node initiated")

		# Create subscriber
		self.talk_sub = rospy.Subscriber("talk", String, self.talk_callback)

	# Callback function for subscriber
	def talk_callback(self, msg):
		rospy.loginfo(msg.data)

if __name__=='__main__':
	n = Listener()
	# Keep node running
	rospy.spin()