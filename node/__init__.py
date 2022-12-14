import copy
from blockchain.utils import Utils
from blockchain.transaction.transaction_pool import TransactionPool
from blockchain.wallet import Wallet
from blockchain.block.blockchain import Blockchain
from node.p2p.message import Message
from node.p2p.message.types import MessageTypes
from node.p2p.socket.socket_communication import SocketCommunication
from node.rest import NodeAPI


class Node():

    def __init__(self, host, port, key=None):
        self.p2p = None
        self.host = host
        self.port = port
        self.transaction_pool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
        if key is not None:
            self.wallet.from_key(key)

    def start_p2p(self):
        self.p2p = SocketCommunication(self.host, self.port)
        self.p2p.start_socket_communication(self)

    def start_api(self, api_port):
        self.api = NodeAPI()
        self.api.inject_node(self)
        self.api.start(api_port)

    def forge(self):
        forger = self.blockchain.next_forger()
        if forger == self.wallet.publicKeyString():
            print('I am the forger.')
            block = self.blockchain.create_block(
                self.transaction_pool.transactions, self.wallet
            )
            self.transaction_pool.remove_from_pool(block.transactions)
            message = Message(
                self.p2p.socket_connector,
                MessageTypes.BLOCK, block
            )
            encoded_message = Utils.encode(message)
            self.p2p.broadcast(encoded_message)
        else:
            print('I am not the forger.')

    def handle_transaction(self, transaction):
        data = transaction.payload()
        signature = transaction.signature
        signer_public_key = transaction.senderPublicKey
        signature_valid = Wallet.signatureValid(
            data, signature, signer_public_key
        )
        transaction_exists = self.transaction_pool.transaction_exists(
            transaction
        )
        transaction_in_block = self.blockchain.transaction_exists(
            transaction
        )
        if not transaction_exists and not transaction_in_block and signature_valid:
            self.transaction_pool.add_transaction(transaction)
            message = Message(
                self.p2p.socket_connector,
                MessageTypes.TRANSACTION, transaction
            )
            encoded_message = Utils.encode(message)
            self.p2p.broadcast(encoded_message)
            forging_required = self.transaction_pool.forger_required()
            if forging_required:
                self.forge()

    def handle_block(self, block):
        forger = block.forger
        block_hash = block.payload()
        signature = block.signature

        block_count_valid = self.blockchain.block_count_valid(block)
        last_block_hash_valid = self.blockchain.last_blockhash_valid(block)
        forger_valid = self.blockchain.forger_valid(block)
        transaction_valid = self.blockchain.transaction_valid(
            block.transactions
        )
        signature_valid = Wallet.signatureValid(block_hash, signature, forger)

        if not block_count_valid:
            self.request_chain()
        if last_block_hash_valid and forger_valid and transaction_valid and signature_valid:
            self.blockchain.add_block(block)
            self.transaction_pool.remove_from_pool(block.transactions)
            message = Message(
                self.p2p.socket_connector,
                MessageTypes.BLOCK, block
            )
            encoded_message = Utils.encode(message)
            self.p2p.broadcast(encoded_message)

    def request_chain(self):
        message = Message(
            self.p2p.socket_connector,
            MessageTypes.BLOCKCHAINREQUEST, None
        )
        encoded_message = Utils.encode(message)
        self.p2p.broadcast(encoded_message)

    def handle_blockchain_request(self, requesting_node):
        message = Message(
            self.p2p.socket_connector,
            MessageTypes.BLOCKCHAIN, self.blockchain
        )
        encoded_message = Utils.encode(message)
        self.p2p.send(requesting_node, encoded_message)

    def handle_blockchain(self, blockchain):
        local_blockchain = copy.deepcopy(self.blockchain)
        local_block_count = len(local_blockchain.blocks)
        received_chain_block_count = len(blockchain.blocks)
        if local_block_count < received_chain_block_count:
            for i, block in enumerate(blockchain.blocks):
                if i >= local_block_count:
                    local_blockchain.add_block(block)
                    self.transaction_pool.remove_from_pool(block.transactions)
            self.blockchain = local_blockchain
