class Bill:

    def __init__(self, amount):
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
        return hash(self.amount)

"""
a = Bill(10)
c = Bill(10)
money_holder = {}

money_holder[a] = 1

if c in money_holder:
    money_holder[c] += 1
print(money_holder)
"""


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        total = 0
        for bill in self.bills:
            total += int(bill)
        return total

    def __int__(self):
        return int(self.total())

    def __str__(self):
        result = ""
        for each in self.bills:
            result = result + str(each)
        return result

"""
values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

for bill in batch:
    print(bill)
"""


class CashDesk:

    def __init__(self):
        self.money = []

    def take_money(self, currency):
        self.money.append(currency)


    def total(self):
        total = 0
        for each in self.money:
            total += int(each)
        return "We have a total of {0}$ in the desk".format(total)

    def inspect(self):
        result_inspectation = {}
        for each in self.money:
            if isinstance(each, BatchBill):
                for ins in each:
                    if ins in result_inspectation:
                        result_inspectation[ins] += 1
                    else:
                        result_inspectation[ins] = 1
            else:
                if each in result_inspectation:
                    result_inspectation[each] += 1
                else:
                    result_inspectation[each] = 1
        print(result_inspectation)

    def __str__(self):
        result = ""
        for each in self.cash_desk:
            result += str(each)
        return result
"""
values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]
batch = BatchBill(bills)
desk = CashDesk()


desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total())
desk.inspect()
"""
