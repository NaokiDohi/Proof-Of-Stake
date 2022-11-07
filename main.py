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

    # Alice wants to send 5 token to Bob.
    transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')

    if not pool.transaction_exists(transaction):
        pool.add_transaction(transaction)

    covered_transaction = block_chain.get_covered_transaction_set(
        pool.transactions)
    print(covered_transaction)
