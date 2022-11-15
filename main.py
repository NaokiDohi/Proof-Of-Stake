from pprint import pprint
from blockchain.utils import Utils
from blockchain.transaction import Transaction
from blockchain.wallet import Wallet
from blockchain.transaction.transaction_pool import TransactionPool
from blockchain.block import Block
from blockchain.block.blockchain import Blockchain
from blockchain.account import AccountModel
from node import Node
import sys

if __name__ == '__main__':

    host = sys.argv[1]
    p2p_port = int(sys.argv[2])
    api_port = int(sys.argv[3])

    node = Node(host, p2p_port)
    node.start_p2p()
    node.start_api(api_port)
