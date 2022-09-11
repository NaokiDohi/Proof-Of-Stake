from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from utils import Utils


class Wallet():

    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        data_hash = Utils.hash(data)
        signature_scheme = PKCS1_v1_5.new(self.keyPair)
        signature = signature_scheme.sign(data_hash)
        return signature.hex()
