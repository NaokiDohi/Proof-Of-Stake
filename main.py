from transaction import Transaction
from wallet import Wallet
from transaction_pool import TransactionPool
from block import Block
from pprint import pprint

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
    pprint(block.to_json())

    signature_valid = Wallet.signatureValid(
        block.payload(), block.signature, wallet.publicKeyString()
    )
    pprint(signature_valid)

    signature_valid = Wallet.signatureValid(
        block.payload(), block.signature, fraudulentWallet.publicKeyString()
    )
    pprint(signature_valid)
