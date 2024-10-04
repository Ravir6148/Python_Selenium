"""
Crate Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.
"""


class Account:
    def __init__(self, balance, accountNo):
        self.balance = balance
        self.accountNo = accountNo

    def debit(self, amount):
        self.balance -= amount
        print(amount, "debited from your account", self.accountNo)
        acca1.bal()

    def credit(self, amount):
        self.balance += amount
        print(amount, "credited in your account", self.accountNo)
        acca1.bal()

    def bal(self):
        print("Your account balance is", self.balance)


acca1 = Account(10000, 8044275767)
acca1.debit(7000)
acca1.credit(4400)
# acca1.bal()
