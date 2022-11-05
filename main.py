from pprint import pprint
from utils import Utils
from transaction import Transaction
from wallet import Wallet
from transaction_pool import TransactionPool
from block import Block
from blockchain import Blockchain
from account_model import AccountModel

if __name__ == '__main__':

    wallet = Wallet()
    account_model = AccountModel()
    # account_model.add_account(wallet.publicKeyString())
    account_model.update_balance(wallet.publicKeyString(), amount=10)
    account_model.update_balance(wallet.publicKeyString(), amount=-5)
    pprint(account_model.balances)
