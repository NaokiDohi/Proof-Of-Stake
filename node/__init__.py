from transaction_pool import TransactionPool
from wallet import Wallet
from blockchain import Blockchain


class Node():

    def __init__(self):
        self.transaction_pool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
