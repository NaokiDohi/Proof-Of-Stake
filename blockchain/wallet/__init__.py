from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from blockchain.utils import Utils
from blockchain.transaction import Transaction
from blockchain.block import Block


class Wallet():

    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def from_key(self, file):
        key = ''
        with open(file, 'r') as keyfile:
            key = RSA.import_key(keyfile.read())
        self.keyPair = key

    def sign(self, data):
        data_hash = Utils.hash(data)
        signature_scheme = PKCS1_v1_5.new(self.keyPair)
        signature = signature_scheme.sign(data_hash)
        return signature.hex()

    @staticmethod
    def signatureValid(data, signature, publicKeyString):
        signature = bytes.fromhex(signature)
        data_Hash = Utils.hash(data)
        public_key = RSA.importKey(publicKeyString)
        signature_scheme = PKCS1_v1_5.new(public_key)
        signature_valid = signature_scheme.verify(data_Hash, signature)
        return signature_valid

    def publicKeyString(self):
        publickey_string = self.keyPair.publickey().exportKey(
            'PEM').decode('utf-8')
        return publickey_string

    def createTransaction(self, reciver, amount, type):
        transaction = Transaction(
            self.publicKeyString(), reciver, amount, type
        )
        # print(f"transaction\n{transaction.to_json()}\n")

        signature = self.sign(transaction.payload())

        # It assign a signature for transaction parameter.
        transaction.sign(signature)
        # print(f"json\n{transaction.to_json()}\npayload\n{transaction.payload()}")
        return transaction

    def createBlock(self, transactions, lastHash, blockCount):
        block = Block(
            transactions, lastHash,
            self.publicKeyString(), blockCount
        )
        signature = self.sign(block.payload())
        block.sign(signature)
        return block
