from p2pnetwork.node import Node


class SocketCommunication(Node):

    def __init__(self, host, port):
        super(SocketCommunication, self).__init__(host, port)

    def start_socket_communication(self):
        self.start()
