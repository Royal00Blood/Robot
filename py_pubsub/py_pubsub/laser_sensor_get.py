import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('py_topic_subscriber_spiral')
        self.subscriber_ = self.create_subscription(LaserScan, '/scan', self.subscribe_message, 1)
        self.subscriber_  # prevent unused variable warning
        self.laser_renge = []

    def subscribe_message(self, msg):
        self.get_logger().info('ranges: %f' % (msg.range_max))
        for i in range(len(msg.ranges)):
            self.laser_renge.append(msg.ranges[i])
        print(self.laser_renge)


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()