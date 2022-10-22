import uuid
import time
import copy


class Transaction():
    def __init__(self, senderPublicKey, reciverPublicKey, amount, type):
        self.senderPublicKey = senderPublicKey
        self.reciverPublicKey = reciverPublicKey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def to_json(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = signature

    def payload(self):
        # deepcopy is used for original data can not changed when we validate signature.
        json_representation = copy.deepcopy(self.to_json())
        json_representation['signature'] = ''
        return json_representation
