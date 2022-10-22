from transaction import Transaction
from wallet import Wallet

if __name__ == '__main__':
    sender = 'sender'
    reciver = 'reciver'
    amount = 1
    type = 'TRANSFER'

    wallet = Wallet()
    # fraudulent_wallet = Wallet()

    transaction = wallet.createTransaction(reciver, amount, type)

    signature_valid = wallet.signatureValid(
        transaction.payload(), transaction.signature, wallet.publicKeyString()
    )
    print(signature_valid)
    # signature_valid = wallet.signatureValid(
    #     transaction.payload(), transaction.signature, fraudulent_wallet.publicKeyString()
    # )
    # print(signature_valid)
