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
    