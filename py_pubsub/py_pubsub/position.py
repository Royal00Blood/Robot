# geometry_msgs/msg/PoseStamped
import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import PoseStamped

class SubPosition(Node):

    def __init__(self):
        super().__init__('position_rob_sub')
        self.subscriber_ = self.create_subscription(PoseStamped, '/goal_pose',self.subscribe_message, 1)
        self.subscriber_
    def subscribe_message(self,msg):
        self.get_logger().info('Recieved - Linear Velocity: %f,Angular Velocity: %f'%(msg.linear.x,msg.angular.z))


def main(args=None):
    rclpy.init(args=args)
    sub = SubPosition()
    rclpy.spin(sub)
    sub.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()