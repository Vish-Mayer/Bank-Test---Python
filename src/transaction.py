from src.transaction_record import Transaction_Record

class Transaction:

    def __init__(self, transaction_record = Transaction_Record, history = []):
        self.transaction_record = transaction_record
        self.history = history

    def credit(self, balance, amount):
        new_balance = balance + amount
        self.__add_to_history(self.transaction_record(balance = new_balance, credit = amount))

    def debit(self, balance, amount):
        new_balance = balance - amount
        self.__add_to_history(self.transaction_record(balance = new_balance, debit = amount))

    def __add_to_history(self, transaction):
        self.history.append(transaction)
