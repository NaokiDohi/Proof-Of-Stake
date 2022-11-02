from pprint import pprint
from transaction import Transaction
from wallet import Wallet
from transaction_pool import TransactionPool
from block import Block
from blockchain import Blockchain

if __name__ == '__main__':
    sender = 'sender'
    reciver = 'reciver'
    amount = 1
    type = 'TRANSFER'

    wallet = Wallet()
    fraudulentWallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(reciver, amount, type)

    if pool.transaction_exists(transaction) == False:
        print("Once")
        pool.add_transaction(transaction)

    block = wallet.createBlock(pool.transactions, 'lastHash', 1)
    # pprint(block.to_json())

    blockchain = Blockchain()
    blockchain.add_block(block)
    pprint(blockchain.to_json())
