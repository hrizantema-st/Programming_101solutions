#from math import abs
def factorial(n):
    result = 1
    for x in range(1, n + 1):
        result = result * x
    return result


def fibonacci(n):
    result = []
    a = 0
    b = 1
    for each in range(1, n + 1):
        tmp = a + b
        a = b
        b = tmp
        result.append(a)
    return result


def sum_of_digits(n):
    helper = abs(n)
    sum = 0
    while helper > 0:
        sum = sum + helper % 10
        helper = helper // 10
    return sum


def sum_of_digits2(n):
    return sum(to_digits(abs(n)))


def fact_digits(n):
    result = 0
    while n > 0:
        tmp = n % 10
        result = result + factorial(tmp)
        n = n // 10
    return result

def factorial_digits2(n):
    return sum([factorial(x) for x in to_digits(n)])


def palindrome(obj):
    return str(obj)[::-1] == str(obj)


def to_digits(n):
    result = []
    while n > 0:
        tmp = n % 10
        result.append(tmp)
        n = n // 10
    return result[::-1]

def to_digits2(n):
    return [int(x) for x in str(n)]

def to_digits3(n):
    b = str(n)
    res = []
    for digit in b:
        res.append (int(digit))
    return res


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_number(digits):
    result = 0
    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit
    return result


def fibonacci_number(n):
    return to_number(fibonacci(n))


def count_vowels(string):
    counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for each in string.lower():
        if each in vowels:
            counter += 1
    return counter


def count_consonants(string):
    counter = 0
    consonants = "bcdfghjklmnpqrstvwxz"
    for each in string.lower():
        if each in consonants:
            counter += 1
    return counter


def char_histogram(string):
    diction = {}
    for each in string:
        if each not in diction:
            diction[each] = 1
        else:
            diction[each] += 1
    return diction


def p_score(n):
    if palindrome(n):
        return 1
    tmp = n + int(str(n)[::-1])
    return 1 + p_score(tmp)



def is_increasing(seq):
    current_len = len(seq)
    boolean = True
    if current_len == 1:
        boolean = True
    else:
        for i in range(0, current_len - 1):
            boolean = boolean and (seq[i] < seq[i + 1])
    return boolean


def is_decreasing(seq):
    current_len = len(seq)
    boolean = True
    if current_len == 1:
        boolean = True
    else:
        for i in range(0, current_len - 1):
            boolean = boolean and (seq[i] > seq[i + 1])
    return boolean


def is_hack(n):
    helper = bin(n)[2:]
    counter = 0
    for each in helper:
        if each == '1':
            counter = counter + 1
    return palindrome(helper) and (counter % 2 != 0)


def even(n):
    return n % 2 == 0


def odd(n):
    return not even(n)


def is_hack2(n):
    binary_n = bin(n)[2:]
    is_palindrome = palindrome(binary_n)
    has_odd_ones = odd(binary_n.count("1"))
    return is_palindrome and has_odd_ones


def next_hack(n):
    n += 1
    while not is_hack(n):
        n += 1
    return n
