#!/usr/bin/env python
import rospy, unittest, rostest
import rosnode
import time

<<<<<<< HEAD
from std_msgs.msg import UInt16

=======
>>>>>>> 2c3fdda9b274313e38c970bfd3b6c495ec72ad54
class BuzzerTest(unittest.TestCase):
	def test_node_exist(self):
		nodes=rosnode.get_node_names()
		self.assertIn('/buzzer', nodes, "node does not exist")

<<<<<<< HEAD
	def test_put_value(self):
		pub = rospy.Publisher('/buzzer', UInt16)
		for i in range(10):
			pub.publish(1234)
			time.sleep(0.1)
		with open("/dev/rtbuzzer0","r") as f:
			data = f.readline()
			self.assertEqual(data,"1234\n","value does not written to rtbuzzer0")

=======
>>>>>>> 2c3fdda9b274313e38c970bfd3b6c495ec72ad54
if __name__ == '__main__':
	time.sleep(3)
	rospy.init_node('travis_test_buzzer')
	rostest.rosrun('pimouse_ros','travis_test_buzzer',BuzzerTest)

