from transaction import Transaction
from wallet import Wallet

if __name__ == '__main__':
    sender = 'sender'
    reciver = 'reciver'
    amount = 1
    type = 'TRANSFER'

    transaction = Transaction(sender, reciver, amount, type)
    # print(transaction)
    print(f"\n{transaction.to_json()}\n")

    wallet = Wallet()
    signature = wallet.sign(transaction.to_json())
    print(signature)

    transaction.sign(signature)
    print(f"\n{transaction.to_json()}\n")
