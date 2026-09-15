import sys
from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        # Wait for the service to actually be running before sending a request
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()
    
    # Grab the two numbers from the terminal command
    response = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    
    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if response.done():
            try:
                result = response.result()
            except Exception as e:
                minimal_client.get_logger().info(f'Service call failed {e}')
            else:
                minimal_client.get_logger().info(
                    f'Result of add_two_ints: for {minimal_client.req.a} + {minimal_client.req.b} = {result.sum}')
            break

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
