def sum_of_divisors(n):
    sum = 0
    for each in range(1, n // 2 + 1):
        if (n % each) == 0:
            sum += each
    sum += n
    return sum


def sum_of_divisors2(n):
    return n + sum([each for each in range(1, n // 2 + 1) if n % each == 0])


def num_of_divisors(n):
    return 1 + sum([1 for each in range(1, n // 2 + 1) if n % each == 0])
"""
print(sum_of_divisors2(8))
print(sum_of_divisors2(7))
print(sum_of_divisors2(1))
print(sum_of_divisors2(1000))
"""


def is_prime(n):
    return sum_of_divisors(n) == (1 + n)
"""
print(is_prime(1))
print(is_prime(2))
print(is_prime(8))
print(is_prime(11))
print(is_prime(-10))
"""


def prime_number_of_divisors(n):
    return is_prime(num_of_divisors(n))
"""
print(prime_number_of_divisors(7))
print(prime_number_of_divisors(8))
print(prime_number_of_divisors(9))
"""


def contains_digit(number, digit):
    helper = False
    while helper == False and number > 0:
        tmp = number % 10
        number = number // 10
        if digit == tmp:
            helper = helper or True
    return helper


def contains_digit2(number, digit):
    return str(digit) in list(str(number))


def contains_digit3(number, digit):
    return digit in to_digits2(number)
"""
print(contains_digit2(123, 4))
print(contains_digit2(42, 2))
print(contains_digit2(1000, 0))
print(contains_digit2(12346789, 5))
"""


def contains_digits(number, digits):
    helper = True
    for each in digits:
        helper = helper and contains_digit2(number, each)
    return helper


def contains_digits2(number, digits):
    for digit in digits:
        if not contains_digits2(number, digit):
            return False
    return True
"""
print(contains_digits(402123, [0, 3, 4]))
print(contains_digits(666, [6,4]))
print(contains_digits(123456789, [1,2,3,0]))
print(contains_digits(456, []))
"""


def to_digits2(n):
    return [int(x) for x in str(n)]


def is_number_balanced(n):
    helper = list(str(n))
    middle = len(str(n)) // 2
    sum1, sum2 = 0, 0
    if len(str(n)) % 2 != 0:
        sum1 += int(helper[middle])
        sum2 += int(helper[middle])
    for i in range(0, middle):
        sum1 = sum1 + int(helper[i])
        sum2 = sum2 + int(helper[len(str(n)) - 1 - i])
    return sum1 == sum2


def is_number_balanced2(n):
    tmp = to_digits2(n)
    if len(tmp) % 2 == 0:
        return sum(tmp[:len(tmp) // 2]) == sum(tmp[len(tmp) // 2:])
    else:
        return sum(tmp[:len(tmp) // 2 + 1]) == sum(tmp[len(tmp) // 2:])


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_number(digits):
    result = 0
    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit
    return result


"""
print(is_number_balanced2(9))
print(is_number_balanced2(11))
print(is_number_balanced2(13))
print(is_number_balanced2(121))
print(is_number_balanced2(4518))
print(is_number_balanced2(28471))
print(is_number_balanced2(1238033))
"""
"""
def count_substrings1(haystack, needle):
    counter = 0
    j = 0
    while j < len(haystack):
        for i in range(0, len(needle)):
            if 
            """


def count_substrings(haystack, needle):
    return haystack.count(needle, 0, len(haystack))
    # return haystack.count(needle)
"""
print(count_substrings("This is a test string", "is"))
print(count_substrings("babababa", "baba"))
print(count_substrings("Python is an awesome language to program in!", "o"))
print(count_substrings("We have nothing in common!", "really?"))
print(count_substrings("This is this and that is this", "this"))
"""


def sum_matrix(m):
    return sum([sum(each) for each in m])
"""
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m))
m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(sum_matrix(m2))
m3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]] 
print(sum_matrix(m3))
"""


def zero_insert(n):
    tmp = list(str(n))
    if len(tmp) > 1:
        for i in range(len(tmp) - 1, 0, -1):
            if tmp[i] == tmp[i - 1] or ((int(tmp[i]) + int(tmp[i - 1])) % 10 == 0):
                tmp.insert(i, '0')
        return int("".join(tmp))
    else:
        return n


def zero_insert2(n):
    result = []
    digits = to_digits(n)
    start = 0
    end = len(digits)
    while start < end - 1:
        x = digits[start]
        y = digits[start + 1]
        result.append(x)
        if (x + y) % 10 == 0 or x == y:
            result.append(0)
        start += 1
    result.append(digits[start])
    return to_number(result)
"""
print(zero_insert(116457))
print(zero_insert(55555555))
print(zero_insert(1))
print(zero_insert(6446))
"""


def bomb(indexes, m):
    i = indexes[0]
    j = indexes[1]
    current_bomb = m[i][j]
    sum_current_matrix = sum_matrix(m)
    adjacents = 0
    if((i == 0 or i == len(m)) and (j == 0 or j == len(m[0]))):
        adjacents += 3
    elif (i == 0 or i == len(m) or j == 0 or j == len(m[0])):
        adjacents += 5
    else:
        adjacents += 8
    sum_current_matrix = sum_current_matrix - adjacents * current_bomb
    return sum_current_matrix


def matrix_bombing_plan(m):
    rows = len(m)
    cols = len(m[0])

    dict_result = {}
    keys = [(x, y) for x in range(0, rows) for y in range(0, cols)]
    for key in keys:
        dict_result[key] = bomb(key, m)

    return dict_result

probichka = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_bombing_plan(probichka))
