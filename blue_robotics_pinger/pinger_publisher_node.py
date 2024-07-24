import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Int32MultiArray
from brping import Ping1D, PingMessage

myPing = Ping1D()
myPing.connect_serial("/dev/ttyUSB0", 115200)
#m = PingMessage()


if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)

class PingerPublisherNode(Node):
    def __init__(self):
        super().__init__('distance_publisher_node')
        self.publisher_ = self.create_publisher(Int32MultiArray, 'pinger', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.distance = 0.0

    def timer_callback(self):
        msg = Int32MultiArray()
        data = myPing.get_distance()
        self.distance = [data["distance"], data["confidence"]]  # Update the distance value
        msg.data = self.distance
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = PingerPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
