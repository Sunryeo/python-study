class BankAccount:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("The balance must not be negative values\n")
        else:
            self._balance = balance
        self._owner = owner

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @owner.setter
    def owner(self, value):
        if self._owner != value:
            raise Exception("Owner cannot be changed!")
        else:
            pass

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("The balance must not be negative values\n")
        else:
            self._balance = value

    def deposit(self, value):
        print(f"Try to deposit {value} to the account")
        if value < 0:
            raise ValueError("Deposit amount must be positive\n")
        else:
            self._balance += value

    def withdraw(self, value):
        print(f"Try to withdraw {value} to the account")
        if value < 0:
            raise ValueError("Withdrawal amount must be positive\n")
        elif self._balance < value:
            raise ValueError(f"Cannot withdraw {value}")
        else:
            self._balance -= value

    def __str__(self):
        printInfo = (f"{'Bank account info':=^39}\n"
                     "%38s" % f"The account owner is {self._owner}\n"
                     "%70s" % f"The current value is {self._balance}\n"
                     "=======================================\n")
        return printInfo


    # pass


if __name__ == '__main__':
    # Create a new account owned by "Alice" with initial balance of -100
    try:
        account_try = BankAccount("Alice", -100)
    except ValueError as e:
        print(e)
    # Create a new account owned by "Alice" with initial balance of 100
    account = BankAccount("Alice", 100)

    # Get owner
    print(f"Owner of the bank account: {account.owner}")
    # Try to change the owner
    try:
        account.owner = "Jinho"
    except Exception as e:
        print(e)

    # Get initial balance
    print(f"The initial balance is {account.balance}")
    # Try to change the initial balance with negative amount
    try:
        account.balance = -100
    except ValueError as e:
        print(e)

# Deposit 50
    account.deposit(50)
    print(account)

    # try to deposit negative value
    try:
        account.deposit(-50)
    except ValueError as e:
        print(e)

    # Try to withdraw 200
    try:
        account.withdraw(200)
    except ValueError as e:
        print(e)
    # The balance should still be 150
    print(account)  # Output: 150
    # Withdraw 100
    account.withdraw(100)
    print(account)  # Output: 50
