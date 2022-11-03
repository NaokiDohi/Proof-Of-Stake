from pprint import pprint
from utils import Utils
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

    blockchain = Blockchain()

    last_hash = Utils().hash(blockchain.blocks[-1].payload()).hexdigest()
    block_count = blockchain.blocks[-1].blockCount + 1
    # block_count = blockchain.blocks[-1].blockCount + 2 # In this pattern, block is not added.
    block = wallet.createBlock(pool.transactions, last_hash, block_count)
    # block = wallet.createBlock(pool.transactions, 'lastHash', block_count) # In this pattern, block is not added.

    if not blockchain.last_blockhash_valid(block):
        print('Lash Blochash is not valid.')
    if not blockchain.block_count_valid(block):
        print('Blockcount is not valid.')

    if blockchain.last_blockhash_valid(block) and blockchain.block_count_valid(block):
        blockchain.add_block(block)

    pprint(blockchain.to_json())
