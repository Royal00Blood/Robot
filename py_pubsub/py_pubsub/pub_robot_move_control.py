import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Robot_control(Node):

    def __init__(self):
        super().__init__("robot_control_node")
        self.cmd_vel_pub_ = self.create_publisher(Twist,"/turtle1/cmd_vel", 10 )
        self.timer_ = self.create_timer(0.5, self.send_velosity_comand)
        #self.get_logger().info("start --> create new control")

    def send_velosity_comand(self):
        msg = Twist()
        msg.linear.x = 2.5
        msg.linear.y = 0.0
        msg.linear.z = 0.0

        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 1.2
        self.cmd_vel_pub_.publish(msg)


def main(args = Node):
    rclpy.init(args=args)
    node = Robot_control()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()



