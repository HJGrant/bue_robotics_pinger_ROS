import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class PingerSubscriberNode(Node):
    def __init__(self):
        super().__init__('ping_subscriber_node')
        self.subscription = self.create_subscription(
            Int32MultiArray,
            'pinger',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Heard: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = PingerSubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
