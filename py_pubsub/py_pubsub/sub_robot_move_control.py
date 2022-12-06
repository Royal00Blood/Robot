import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist

class MinimalpSubscriber(Node):

    def __init__(self):
        super().__init__('py_topic_sub_robot')
        self.subscriber_ = self.create_subscription(Twist, '/cmd_vel',self.subscribe_message, 1)
        self.subscriber_
    def subscribe_message(self,msg):
        self.get_logger().info('Recieved - Linear Velocity: %f,Angular Velocity: %f'%(msg.linear.x,msg.angular.z))


def main(args=None):
    rclpy.init(args=args)
    sub = MinimalpSubscriber()
    rclpy.spin(sub)
    sub.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()