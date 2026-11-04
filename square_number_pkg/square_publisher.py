import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class SquarePublisher(Node):

    def __init__(self):
        super().__init__('square_publisher')
        self.publisher = self.create_publisher(Int32, 'square_numbers', 10)
        self.counter = 1
        self.timer = self.create_timer(1.0, self.publish_square)

    def publish_square(self):
        msg = Int32()
        square = self.counter**2
        msg.data = square
        self.publisher.publish(msg)
        
        self.get_logger().info(f'Number : {self.counter}, Square: {square}')

        if self.counter>=10:
             self.counter =1
        else:
            self.counter+=1


def main(args=None):

    rclpy.init(args=args)

    node = SquarePublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
