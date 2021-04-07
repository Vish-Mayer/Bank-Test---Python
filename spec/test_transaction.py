import unittest
from unittest import mock
from src.transaction import Transaction

class Transaction_Test(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction()
        self.transaction.transaction_record = mock.Mock(name="transaction_record")

    def test_credit(self):
        self.transaction.credit(0, 10)
        self.transaction.transaction_record.assert_called_once_with(balance=10, credit=10)
        self.assertEqual(len(self.transaction.history), 1)
