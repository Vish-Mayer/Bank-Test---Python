import unittest
from src.transaction_record import Transaction_Record

class Transaction_Record_Test(unittest.TestCase):

    def setUp(self):
        self.transaction_record = Transaction_Record(date = "01-04-2021", credit = 10, debit = None, balance = 10)

    def test_date(self):
        self.assertEqual(self.transaction_record.date, '01-04-2021')

    def test_credit(self):
        self.assertEqual(self.transaction_record.credit, 10)

    def test_debit(self):
        self.assertEqual(self.transaction_record.credit, None)

    def test_debit(self):
        self.assertEqual(self.transaction_record.credit, 10)
