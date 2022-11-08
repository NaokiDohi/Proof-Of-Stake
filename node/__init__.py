from transaction_pool import TransactionPool
from wallet import Wallet
from blockchain import Blockchain
from node.socket.socket_communication import SocketCommunication


class Node():

    def __init__(self, host, port):
        self.p2p = None
        self.host = host
        self.port = port
        self.transaction_pool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()

    def start_p2p(self):
        self.p2p = SocketCommunication(self.host, self.port)
        self.p2p.start_socket_communication()
