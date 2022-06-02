# Add these methods to class Account - deposit, withdraw.
#  Create two instances of account and verify they work as expected.

class Account:
    def __init__(self,balance,account_number,account_name):
        self.balance = balance
        self.account_number = account_number
        self.account_name = account_name

    def deposit(self,deposits):
        self.balance+=deposits
        return self.balance
    
    def withdraw(self,withdraw):
        self.balance -= withdraw
        return self.balance
    