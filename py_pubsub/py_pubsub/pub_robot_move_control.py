import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalPublisher(Node):

    def __init__(self,x =0 ,y = 0,z = 0,ang_x = 0,ang_y = 0,ang_z = 0):
        super().__init__('py_topic_publisher_spiral')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 1)
        timer_period = 0.5  # seconds
        self.i = 0.0
        self.timer_ = self.create_timer(timer_period, self.publish_message)
        self.x = x
        self.y = y
        self.z = z
        self.ang_x = ang_x
        self.ang_y = ang_y
        self.ang_z = ang_z

    def publish_message(self):
        message = Twist()
        message.linear.x = float(self.x)
        message.linear.y = float(self.y)
        message.linear.z = float(self.z)
        message.angular.x = float(self.ang_x)
        message.angular.y = float(self.ang_y)
        message.angular.z = float(self.ang_z)
        self.get_logger().info('Sending - Linear Velocity : %f, Angular Velocity : %f' % (message.linear.x, message.angular.z))
        self.publisher_.publish(message)
        self.i += 0.1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher(0.1,0,0,0,0,0)
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()