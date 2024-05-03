class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("The balance must not be negative values")
        else:
            self._balance = value

    def deposit(self, value):
        if value < 0:
            raise ValueError("Deposit amount must be positive")
        else:
            self._balance += value

    def withdraw(self, value):
        if value < 0:
            raise ValueError("Withdrawal amount must be positive")
        elif value > self._balance:
            raise ValueError("Out of balance")
        else:
            self._balance -= value

    def __str__(self):
        printInfo = (f"{'Bank account info':=^39}\n"
                     "%38s" % f"The account owner is {self._owner}\n"
                     "%70s" % f"The current value is {self._balance}\n"
                     "=======================================\n")
        return printInfo
