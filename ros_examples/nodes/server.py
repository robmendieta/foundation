#!/usr/bin/env python

import rospy
import numpy as np
from ros_examples.srv import TwoInts

class Server:
	def __init__ (self):
		# Init node
		rospy.init_node("addTwoInts_server")
		rospy.loginfo("addTwoInts_server node initiated")

		# Create service
		self.addTwoInts_srv = rospy.Service("addTwoInts", TwoInts, self.addTwoInts_handle)

	# Service handle, executed each time a request is received
	def addTwoInts_handle(self, req):
		print "First int: ", req.A
		print "Second int: ", req.B
		result = req.A + req.B
		print "Result: ", result
		return result

if __name__=='__main__':
	n = Server()
	# Keep node running
	rospy.spin()