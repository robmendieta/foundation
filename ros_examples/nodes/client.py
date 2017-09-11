#!/usr/bin/env python

import rospy
import numpy as np
from ros_examples.srv import TwoInts

class Client:
	def __init__ (self):
		# Init node
		rospy.init_node("addTwoInts_client")
		rospy.loginfo("addTwoInts_client node initiated")

		# Wait until the service is advertised
		rospy.wait_for_service("addTwoInts")

		# Create a client to the service
		self.addTwoInts_client = rospy.ServiceProxy("addTwoInts", TwoInts)

if __name__=='__main__':
	n = Client()
	rate = rospy.Rate(1)

	# Keep looping and asking for input
	while not rospy.is_shutdown():
		try:
			A = int(raw_input("Enter int A: "))
		except ValueError:
			A = 0

		try: 
			B = int(raw_input("Enter int B: "))
		except ValueError:
			B = 0

		# Call service client, arguments are request and returns results
		print n.addTwoInts_client(A, B)
		rate.sleep()