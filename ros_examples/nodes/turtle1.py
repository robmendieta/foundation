#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class Talker:
	def __init__ (self):
		# Init node
		rospy.init_node("talker")
		rospy.loginfo("Talker node initiated")

		# Create publisher
		self.talk_pub = rospy.Publisher("talk", String, queue_size = 10)
		# Create empty message
		self.talk_msg = String()
		
		# Turtle
		self.twist_pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size = 10)
		# Create empty message
		self.twist_msg = Twist()

	def talk(self):
		# Create message from user input
		self.talk_msg = raw_input("Enter a message: ")
		# Publish message
		self.talk_pub.publish(self.talk_msg)

	def move(self):
		self.twist_msg.linear.x = float(raw_input("Enter lin x: "))
		self.twist_msg.linear.y = float(raw_input("Enter lin y: "))
		self.twist_msg.angular.z = float(raw_input("Enter ang z: "))
		# Publish message
		self.twist_pub.publish(self.twist_msg)		

if __name__=='__main__':
	n = Talker()
	rate = rospy.Rate(1)
	# Keep looping and asking for input
	while not rospy.is_shutdown():
		#n.talk()
		n.move()
		rate.sleep()
	