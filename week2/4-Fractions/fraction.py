class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator
"""
    def __truediv___(self, other):
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator)
"""

"""
a = Fraction(1, 2)
b = Fraction(2, 4)

print(a == b) # True
c = a + b
d = a - b
e = a * b
print(c) # 1
print(d) # 0
print(e)
"""
