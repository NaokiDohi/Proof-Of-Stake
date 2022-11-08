from p2pnetwork.node import Node


class SocketCommunication(Node):

    def __init__(self, host, port):
        super(SocketCommunication, self).__init__(host, port)

    def start_socket_communication(self):
        self.start()

    def inbound_node_connected(self, connected_node):
        print('Inbound Connection')
        self.send_to_node(
            connected_node,
            'Hi! I am the node you connected to.'
        )

    def outbound_node_connected(self, connected_node):
        print('Outbound Connection')
        self.send_to_node(
            connected_node,
            'Hi! I am the node who initialized the connection.'
        )

    def node_message(self, connected_node, message):
        print(message)
