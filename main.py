from pprint import pprint
from utils import Utils
from transaction import Transaction
from wallet import Wallet
from transaction_pool import TransactionPool
from block import Block
from blockchain import Blockchain
from account_model import AccountModel
from node import Node

if __name__ == '__main__':
    node = Node()
    print(F'{node.blockchain}\n{node.transaction_pool}\n{node.wallet}')
