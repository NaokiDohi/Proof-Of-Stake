from wallet import Wallet
from utils import Utils
import requests

if __name__ == '__main__':
    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()

    transaction = exchange.createTransaction(
        alice.publicKeyString(), 10, 'EXCHANGE'
    )

    url = 'http://localhost:5001/transaction'
    package = {'transaction': Utils.encode(transaction)}
    request = requests.post(url, json=package)
    print(request.text)
