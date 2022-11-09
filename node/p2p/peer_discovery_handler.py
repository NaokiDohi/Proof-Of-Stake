import time
import threading


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
        self.socket_communication.send(connected_node, 'Handshake ...')
