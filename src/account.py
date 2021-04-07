from src.transaction import Transaction

class Bank_Account:

    def __init__(self, balance=0, transaction = Transaction()):
        self.balance = 0
        self.transaction = transaction

    def deposit(self, amount):
        self.transaction.credit(self.balance, amount)
        self.balance += amount

    def withdraw(self, amount):
        self.transaction.debit(self.balance, amount)
        self.balance -= amount
