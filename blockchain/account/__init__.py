class AccountModel():

    def __init__(self):
        # accounts variable is list involved all participate of chain.
        self.accounts = []
        # balances variable is for mapping balances from key of account.
        self.balances = {}

    def add_account(self, public_key_string):
        """ Register the publick key to self.accounts

        Keyword arguments:
        public_key_string -- This means public key of string type.
        Return: None

        """

        # Check account already exists or not.
        if not public_key_string in self.accounts:
            self.accounts.append(public_key_string)
            # set the initial balances for new accounts.
            self.balances[public_key_string] = 0

    def get_balances(self, public_key_string):
        if public_key_string not in self.accounts:
            self.add_account(public_key_string)
        return self.balances[public_key_string]

    def update_balance(self, public_key_string, amount):
        if public_key_string not in self.balances:
            self.add_account(public_key_string)
        self.balances[public_key_string] += amount
