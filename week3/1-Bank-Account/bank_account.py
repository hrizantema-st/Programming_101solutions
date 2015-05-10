class BankAccount:

    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError
        if not isinstance(balance, int):
            raise TypeError

        self.name = name
        self.balance = balance
        self.currency = currency

    def __int__(self):
        return self.balance

    def __str__(self):
        message = "Bank account for {0} with balance of {1}{2}"
        return message.format(self.name, self.balance, self.currency)

    def __repr__(self):
        return self.__str__()

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError

        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            return False
        else:
            self.balance -= amount
            return True

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError

        if self.balance < amount:
            return False

        self.balance -= amount
        account.balance += amount
        return True
