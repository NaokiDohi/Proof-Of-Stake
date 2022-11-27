from blockchain.block import Block
from blockchain.utils import Utils
from blockchain.account import AccountModel
from blockchain.pos import ProofOfStake


class Blockchain():
    def __init__(self):
        self.blocks = [Block.genesis()]
        self.account_model = AccountModel()
        self.pos = ProofOfStake()

    def add_block(self, block):
        self.execute_transactions(block.transactions)
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
        if transaction.type == 'EXCHANGE':
            return True

        sender_blance = self.account_model.get_balances(
            transaction.senderPublicKey
        )

        if sender_blance >= transaction.amount:
            return True
        else:
            return False

    def execute_transactions(self, transactions):
        for transaction in transactions:
            self.execute_transaction(transaction)

    def execute_transaction(self, transaction):
        if transaction.type == 'STAKE':
            sender = transaction.senderPublicKey
            receiver = transaction.receiverPublicKey
            if sender == receiver:
                amount = transaction.amount
                self.pos.update(sender, amount)
                self.account_model.update_balance(sender, -amount)
        else:
            sender = transaction.senderPublicKey
            receiver = transaction.reciverPublicKey
            amount = transaction.amount
            self.account_model.update_balance(sender, -amount)
            self.account_model.update_balance(receiver, amount)

    def next_forger(self):
        last_block_hash = Utils.hash(self.blocks[-1].payload()).hexdigest()
        next_forger = self.pos.forger(last_block_hash)
        return next_forger

    def create_block(self, transaction_from_pool, forger_wallet):
        covered_transactions = self.get_covered_transaction_set(
            transaction_from_pool
        )
        self.execute_transactions(covered_transactions)
        new_block = forger_wallet.createBlock(
            covered_transactions,
            Utils.hash(self.blocks[-1].payload()).hexdigest(),
            len(self.blocks)
        )
        self.blocks.append(new_block)
        return new_block

    def transaction_exists(self, transaction):
        for block in self.blocks:
            for block_transaction in block.transactions:
                if transaction.equals(block_transaction):
                    return True
        return False
