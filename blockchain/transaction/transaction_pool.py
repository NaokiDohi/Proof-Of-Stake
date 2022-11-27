class TransactionPool():

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def transaction_exists(self, transaction):
        for pool_transaction in self.transactions:
            if pool_transaction.equals(transaction):
                return True
        return False

    def remove_from_pool(self, transactions):
        pool_transactions = []
        for pool_transaction in self.transactions:
            insert = True
            for transaction in transactions:
                if pool_transaction.equals(transaction):
                    insert = False
            if insert:
                pool_transactions.append(transaction)
        self.transactions = pool_transactions

    def forger_required(self):
        if len(self.transactions) >= 1:
            return True
        else:
            return False
