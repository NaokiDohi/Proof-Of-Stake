from transaction import Transaction
from wallet import Wallet
from transaction_pool import TransactionPool

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

    if pool.transaction_exists(transaction) == False:
        # Transactions are already exist. So, it is not called.
        print("Twice")
        pool.add_transaction(transaction)

    print(pool.transactions)
