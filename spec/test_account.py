import unittest
from src.account import Bank_Account

class Bank_Account_Test(unittest.TestCase):

    def setUp(self):
        self.account = Bank_Account()

    def test_default_balance(self):
        self.assertEqual(self.account.balance, 0)

    def test_deposit(self):
        self.account.deposit(10)
        self.assertEqual(self.account.balance, 10)

    def test_withdraw(self):
        self.account.deposit(10)
        self.account.withdraw(5)
        self.assertEqual(self.account.balance, 5)
