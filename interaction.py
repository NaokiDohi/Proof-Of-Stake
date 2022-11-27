from blockchain.wallet import Wallet
from blockchain.utils import Utils
import requests


def post_transaction(sender, receiver, amount, type):
    transaction = sender.createTransaction(
        receiver.publicKeyString(), amount, type
    )
    url = 'http://localhost:5001/transaction'
    package = {'transaction': Utils.encode(transaction)}
    request = requests.post(url, json=package)
    print(request.text)


if __name__ == '__main__':
    alice = Wallet()
    alice.from_key('keys/stakerPrivateKey.pem')
    bob = Wallet()
    exchange = Wallet()

    # forger: genesis
    post_transaction(exchange, alice, 100, 'EXCHANGE')
    post_transaction(exchange, bob, 100, 'EXCHANGE')
    post_transaction(alice, alice, 25, 'STAKE')

    # forger: probably alice
    post_transaction(alice, bob, 1, 'TRANFER')
