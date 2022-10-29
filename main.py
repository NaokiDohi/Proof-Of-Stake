from transaction import Transaction
from wallet import Wallet
from transaction_pool import TransactionPool
from block import Block

if __name__ == '__main__':
    sender = 'sender'
    reciver = 'reciver'
    amount = 1
    type = 'TRANSFER'

    wallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(reciver, amount, type)

    if pool.transaction_exists(transaction) == False:
        print("Once")
        pool.add_transaction(transaction)

    block = Block(pool.transactions, "lastHash", "forger", 1)

    print(block.to_json())
