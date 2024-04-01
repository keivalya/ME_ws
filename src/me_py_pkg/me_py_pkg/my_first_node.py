#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("CSKvsGT") # naming of the node
        # TO-DO!
        self.get_logger().info("I am Gujju, but I am still a huge Mahi fan!")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== '__main__':
    main()