#!/usr/bin/env python3

class Bank_Account:

    def __init__(self, balance=0):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
