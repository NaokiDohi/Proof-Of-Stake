from transaction_pool import TransactionPool
from wallet import Wallet
from blockchain import Blockchain
from node.p2p.socket.socket_communication import SocketCommunication
from node.rest import NodeAPI


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

    def start_api(self, api_port):
        self.api = NodeAPI()
        self.api.start(api_port)
