import time
import copy


class Block():
    def __init__(self, transactions, lastHash, forger, blockCount):
        self.transactions = transactions
        self.lastHash = lastHash
        self.forger = forger
        self.blockCount = blockCount
        self.timestamp = time.time()
        self.signature = ''

    @staticmethod
    def genesis():
        genesis_block = Block([], 'genesisHash', 'genesis', 0)
        # You need to override the timestamp. Because, it is changed when it is every initialized.
        genesis_block.timestamp = 0
        return genesis_block

    def to_json(self):
        # The reason why use self.__dict__, it is self.transactions get instance.
        data = {}
        data['lastHash'] = self.lastHash
        data['forger'] = self.forger
        data['blockCount'] = self.blockCount
        data['timestamp'] = self.timestamp
        data['signature'] = self.signature
        jsonTransactions = []
        for transaction in self.transactions:
            jsonTransactions.append(transaction.to_json())
        data['transactions'] = jsonTransactions
        return data

    def payload(self):
        jsonRepresentation = copy.deepcopy(self.to_json())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

    def sign(self, signature):
        self.signature = signature
