class Bill:

    def __init__(self, amount):
        if amount <= 0:
            raise ValueError
        if not isinstance(amount, int):
            raise TypeError
        self.amount = amount

    def ___str___(self):
        return str(self.amount)

    def __repr__(self):
        return str(self.amount)

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.__str__())
