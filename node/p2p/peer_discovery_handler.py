import time
import threading
from utils import Utils
from node.message import Message


class PeerDiscoveryHandler():

    def __init__(self, node):
        self.socket_communication = node

    def start(self):
        status_thread = threading.Thread(target=self.status, args=())
        status_thread.start()
        discovery_thread = threading.Thread(target=self.discovery, args=())
        discovery_thread.start()

    def status(self):
        """
            Broadcast the message of status.
        """

        while True:
            print("Status!!")
            time.sleep(10)

    def discovery(self):
        """
            Broadcast the message.
        """

        while True:
            print("Discovery!!")
            time.sleep(10)

    def handshake(self, connected_node):
        handshake_message = self.handshake_message()
        self.socket_communication.send(connected_node, handshake_message)

    def handshake_message(self):
        own_connector = self.socket_communication.socket_connector
        own_peers = self.socket_communication.peers
        data = own_peers
        message_type = 'DISCOVERY'
        message = Message(own_connector, message_type, data)
        encoded_message = Utils().encode(message)
        return encoded_message
