import json
from p2pnetwork.node import Node
from utils import Utils
from node.p2p.peer_discovery_handler import PeerDiscoveryHandler
from node.p2p.socket.socket_connector import SocketConnector


class SocketCommunication(Node):

    def __init__(self, host, port):
        super(SocketCommunication, self).__init__(host, port)
        self.peers = []
        self.peer_discovery_handler = PeerDiscoveryHandler(self)
        self.socket_connector = SocketConnector(host, port)

    def connect_to_first_node(self):
        if self.socket_connector.port != 10001:
            self.connect_with_node('localhost', 10001)

    def start_socket_communication(self, node):
        self.node = node
        self.start()
        self.peer_discovery_handler.start()
        self.connect_to_first_node()

    def inbound_node_connected(self, connected_node):
        self.peer_discovery_handler.handshake(connected_node)

    def outbound_node_connected(self, connected_node):
        self.peer_discovery_handler.handshake(connected_node)

    def node_message(self, connected_node, message):
        message = Utils().decode(json.dumps(message))
        if message.message_type == 'DISCOVERY':
            self.peer_discovery_handler.handle_message(message)
        elif message.message_type == 'TRANSACTION':
            transaction = message.data
            self.node.handle_transaction(transaction)

    def send(self, receiver, message):
        self.send_to_node(receiver, message)

    def broadcast(self, message):
        self.send_to_nodes(message)
