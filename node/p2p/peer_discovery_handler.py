import time
import threading
from blockchain.utils import Utils
from node.p2p.message import Message
from node.p2p.message.types import MessageTypes


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
            print("Current Connections:")
            for peer in self.socket_communication.peers:
                print(f'{peer.host}:{peer.port}')
            time.sleep(10)

    def discovery(self):
        """
            Broadcast the message.
        """

        while True:
            print("Discovery!!")
            handshake_message = self.handshake_message()
            self.socket_communication.broadcast(handshake_message)
            time.sleep(10)

    def handshake(self, connected_node):
        handshake_message = self.handshake_message()
        self.socket_communication.send(connected_node, handshake_message)

    def handshake_message(self):
        own_connector = self.socket_communication.socket_connector
        own_peers = self.socket_communication.peers
        data = own_peers
        message_types = MessageTypes.DISCOVERY
        message = Message(own_connector, message_types, data)
        encoded_message = Utils().encode(message)
        return encoded_message

    def handle_message(self, message):
        peers_socket_connector = message.sender_connector
        peers_peer_list = message.data
        new_peer = True
        for peer in self.socket_communication.peers:
            if peer.equals(peers_socket_connector):
                new_peer = False
        if new_peer:
            self.socket_communication.peers.append(peers_socket_connector)

        for peers_peer in peers_peer_list:
            peer_known = False
            for peer in self.socket_communication.peers:
                if peer.equals(peers_peer):
                    peer_known = True
            if not peer_known and not peers_peer.equals(self.socket_communication.socket_connector):
                self.socket_communication.connect_with_node(
                    peers_peer.host, peers_peer.port
                )
