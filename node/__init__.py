from blockchain.utils import Utils
from blockchain.transaction.transaction_pool import TransactionPool
from blockchain.wallet import Wallet
from blockchain.block.blockchain import Blockchain
from node.p2p.message import Message
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
        self.p2p.start_socket_communication(self)

    def start_api(self, api_port):
        self.api = NodeAPI()
        self.api.inject_node(self)
        self.api.start(api_port)

    def handle_transaction(self, transaction):
        data = transaction.payload()
        signature = transaction.signature
        signer_public_key = transaction.senderPublicKey
        signature_valid = Wallet.signatureValid(
            data, signature, signer_public_key
        )
        transaction_exists = self.transaction_pool.transaction_exists(
            transaction)
        if not transaction_exists and signature_valid:
            self.transaction_pool.add_transaction(transaction)
            message = Message(
                self.p2p.socket_connector,
                'TRANSACTION', transaction
            )
            encoded_message = Utils.encode(message)
            self.p2p.broadcast(encoded_message)
