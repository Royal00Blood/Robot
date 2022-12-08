import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist
import numpy as np
import random as r


class Node_in_out(Node):

    def __init__(self,x =0 ,y = 0,z = 0,ang_x = 0,ang_y = 0,ang_z = 0):
        super().__init__('rundom_rase')
        self.sub_ = self.create_subscription(Twist, '/cmd_vel',self.callback_data, 10)
        self.pub_ = self.create_publisher(Twist, '/cmd_vel', 10)
        # timer_period = 0.5  # seconds
        # self.i = 0.0
        # self.timer_ = self.create_timer(timer_period, self.callback_data)
    
    def callback_data(self,msg):
        # self.get_logger().info('Start_Recieved - Linear Velocity: %f,Angular Velocity: %f'%(msg.linear.x,msg.angular.z))
        new_msg = Twist()
        new_msg.linear.x = msg.linear.x + r.triangular(-1,1,0.1)
        new_msg.linear.y = 0.0
        new_msg.linear.z = 0.0
        new_msg.angular.z = msg.angular.z + r.triangular(-1,1,0.1)
        new_msg.angular.y = 0.0
        new_msg.angular.x = 0.0
        # self.get_logger().info('After_Recieved - Linear Velocity: %f,Angular Velocity: %f'%(msg.linear.x,msg.angular.z))
        self.pub_.publish(new_msg)
        # self.i += 0.1

    # def subscribe_message(self,msg):
    #     self.get_logger().info('Recieved - Linear Velocity: %f,Angular Velocity: %f'%(msg.linear.x,msg.angular.z))

    # def pubsub_message(self,msg):
    #     message = Twist()
    #     z_angle =  message.angular.z + np.random.randrange(-1,1,0.1)
    #     x_line =  message.linear.x + np.random.randrange(-1,1,0.1)
    #     message.linear.x = float(z_angle)
    #     message.linear.y = float(self.y)
    #     message.linear.z = float(self.z)
    #     message.angular.x = float(self.ang_x)
    #     message.angular.y = float(self.ang_y)
    #     message.angular.z = float(x_line)
    #     self.get_logger().info('Sending - Linear Velocity : %f, Angular Velocity : %f' % (message.linear.x, message.angular.z))
    #     self.publisher_.publish(message)
    #     self.i += 0.1

def main(args=None):
    rclpy.init(args=args)
    run = Node_in_out(0.1,0,0,0,0,0)
    rclpy.spin(run)
    run.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()