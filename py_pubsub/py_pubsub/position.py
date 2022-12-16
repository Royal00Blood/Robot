# geometry_msgs/msg/PoseStamped
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('py_topic_subscriber_spiral')
        self.subscriber_ = self.create_subscription(Odometry, '/odom', self.subscribe_message, 1)
        self.subscriber_  # prevent unused variable warning
        

    def subscribe_message(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        q1 = msg.pose.pose.orientation.x
        q2 = msg.pose.pose.orientation.y
        q3 = msg.pose.pose.orientation.z
        q4 = msg.pose.pose.orientation.w
        self.get_logger().info('ranges: %f' % (msg.pose.pose.position.x))


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()