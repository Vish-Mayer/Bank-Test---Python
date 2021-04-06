import unittest
from src.account import Bank_Account

class Bank_Account_Test(unittest.TestCase):

    def test_default_balance(self):
        self.account = Bank_Account()
        self.assertEqual(self.account.balance, 0)

    def test_deposit(self):
        self.account = Bank_Account()
        self.account.deposit(10)
        self.assertEqual(self.account.balance, 10)

    
