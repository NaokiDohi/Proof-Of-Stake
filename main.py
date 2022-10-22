from transaction import Transaction
from wallet import Wallet

if __name__ == '__main__':
    sender = 'sender'
    reciver = 'reciver'
    amount = 1
    type = 'TRANSFER'

    transaction = Transaction(sender, reciver, amount, type)
    # print(f"transaction\n{transaction.to_json()}\n")

    wallet = Wallet()
    signature = wallet.sign(transaction.to_json())
    # print(signature)

    # It assign a signature for transaction parameter.
    transaction.sign(signature)
    # print(f"\n{transaction.to_json()}\n")

    signature_valid = Wallet.signatureValid(
        transaction.payload(), signature, wallet.publicKeyString()
    )
    print(signature_valid)
    print(f"\n{transaction.to_json()}\n")
