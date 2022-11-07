from pprint import pprint
from utils import Utils
from transaction import Transaction
from wallet import Wallet
from transaction_pool import TransactionPool
from block import Block
from blockchain import Blockchain
from account_model import AccountModel

if __name__ == '__main__':

    block_chain = Blockchain()
    pool = TransactionPool()

    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()
    forger = Wallet()

    exchange_transaction = exchange.createTransaction(
        alice.publicKeyString(), 10, 'EXCHANGE'
    )

    if not pool.transaction_exists(exchange_transaction):
        pool.add_transaction(exchange_transaction)

    covered_transaction = block_chain.get_covered_transaction_set(
        pool.transactions
    )
    last_hash = Utils().hash(block_chain.blocks[-1].payload()).hexdigest()
    block_count = block_chain.blocks[-1].blockCount + 1
    block_one = Block(
        covered_transaction, last_hash,
        forger.publicKeyString(), block_count
    )
    block_chain.add_block(block_one)

    # Alice wants to send 5 token to Bob.
    transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')

    if not pool.transaction_exists(transaction):
        pool.add_transaction(transaction)

    covered_transaction = block_chain.get_covered_transaction_set(
        pool.transactions
    )
    last_hash = Utils().hash(block_chain.blocks[-1].payload()).hexdigest()
    block_count = block_chain.blocks[-1].blockCount + 1
    block_two = Block(
        covered_transaction, last_hash,
        forger.publicKeyString(), block_count
    )
    block_chain.add_block(block_two)

    pprint(block_chain.to_json())
