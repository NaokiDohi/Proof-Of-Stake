from Transaction import Transaction

if __name__ == '__main__':
    sender = 'sender'
    reciver = 'reciver'
    amount = 1
    type = 'TRANSFER'

    transaction = Transaction(sender, reciver, amount, type)
    print(transaction)
    print(transaction.to_json())