# import sys
# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist

# class Robot_control(Node):

#     def __init__(self):
#         super().__init__("robot_control_node")
#         self.cmd_vel_pub_ = self.create_publisher(Twist,'robot_first/cmd_vel', 1 )
#         self.timer_ = self.create_timer(0.5, self.send_velosity_comand)
#         self.get_logger().info("start --> create new control")

#     def send_velosity_comand(self):
#         msg = Twist()
#         msg.linear.x = float(sys.argv[1])
#         msg.angular.z = float(sys.argv[2])
#         self.cmd_vel_pub_.publish(msg)


# def main(args = Node):
#     rclpy.init(args=args)
#     node = Robot_control()
#     rclpy.spin(node)
#     rclpy.shutdown()

# if __name__=='__main__':
#     main()



import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('py_topic_publisher_spiral')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 1)
        timer_period = 0.5  # seconds
        self.i = 0.0
        self.timer_ = self.create_timer(timer_period, self.publish_message)

    def publish_message(self):
        message = Twist()
        x = 3.5
        z = 0.0
        message.linear.x = float(x)
        message.angular.z = float(z)
        self.get_logger().info('Sending - Linear Velocity : %f, Angular Velocity : %f' % (message.linear.x, message.angular.z))
        self.publisher_.publish(message)
        self.i += 0.1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()