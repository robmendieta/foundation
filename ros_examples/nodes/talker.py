#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String


class Talker:
	def __init__ (self):
		# Init node
		rospy.init_node("talker")
		rospy.loginfo("Talker node initiated")

		# Create publisher
		self.talk_pub = rospy.Publisher("talk", String, queue_size = 10)
		# Create empty message
		self.talk_msg = String()

	def talk(self):
		# Create message from user input
		self.talk_msg = raw_input("Enter a message: ")
		# Publish message
		self.talk_pub.publish(self.talk_msg)


if __name__=='__main__':
	n = Talker()
	rate = rospy.Rate(1)
	# Keep looping and asking for input
	while not rospy.is_shutdown():
		n.talk()
		rate.sleep()
	