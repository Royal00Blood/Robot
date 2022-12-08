import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist
import numpy as np
import random as r
import DDPG as dd

state = [0,0,0,0,0,0]
class Node_in_out(Node):

    def __init__(self,x =0 ,y = 0,z = 0,ang_x = 0,ang_y = 0,ang_z = 0):
        super().__init__('rundom_rase')
        self.sub_ = self.create_subscription(Twist, '/cmd_vel',self.callback_data, 10)
        self.pub_ = self.create_publisher(Twist, '/cmd_vel', 10)
    
    def callback_data(self,msg):
        new_msg = Twist()
        state[0],state[1],state[2],state[3],state[4],state[5] = msg.linear.x, msg.linear.y, msg.linear.z, msg.angular.x, msg.angular.y, msg.angular.z
        dd.Env_take_info()
        new_msg.linear.x = msg.linear.x + r.triangular(-1,1,0.1)
        new_msg.linear.y = 0.0
        new_msg.linear.z = 0.0
        new_msg.angular.z = msg.angular.z + r.triangular(-1,1,0.1)
        new_msg.angular.y = 0.0
        new_msg.angular.x = 0.0
        self.pub_.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    run = Node_in_out(0.1,0,0,0,0,0)
    rclpy.spin(run)
    run.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()