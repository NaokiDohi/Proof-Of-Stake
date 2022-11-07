from block import Block
from utils import Utils
from account_model import AccountModel


class Blockchain():
    def __init__(self):
        self.blocks = [Block.genesis()]
        self.account_model = AccountModel()

    def add_block(self, block):
        self.blocks.append(block)

    def to_json(self):
        data = {}
        json_blocks = []
        for block in self.blocks:
            json_blocks.append(block.to_json())
        data['blocks'] = json_blocks
        return data

    def block_count_valid(self, block):
        if self.blocks[-1].blockCount == block.blockCount-1:
            return True
        else:
            return False

    def last_blockhash_valid(self, block):
        latest_blockchain_blockhash = Utils().hash(
            self.blocks[-1].payload()).hexdigest()
        if latest_blockchain_blockhash == block.lastHash:
            return True
        else:
            return False

    def get_covered_transaction_set(self, transactions):
        covered_transactions = []
        for transaction in transactions:
            if self.transaction_covered(transaction):
                covered_transactions.append(transaction)
            else:
                print('Transaction is not covered by sender.')
        return covered_transactions

    def transaction_covered(self, transaction):
        if transaction.type == 'EXCHAGE':
            return True

        sender_blance = self.account_model.get_balances(
            transaction.senderPublicKey
        )

        if sender_blance >= transaction.amount:
            return True
        else:
            return False
