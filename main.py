from pprint import pprint
from utils import Utils
from transaction import Transaction
from wallet import Wallet
from transaction_pool import TransactionPool
from block import Block
from blockchain import Blockchain
from account_model import AccountModel
from node import Node
import sys

if __name__ == '__main__':

    host = sys.argv[1]
    p2p_port = int(sys.argv[2])
    api_port = int(sys.argv[3])

    node = Node(host, p2p_port)
    node.start_p2p()
    node.start_api(api_port)
