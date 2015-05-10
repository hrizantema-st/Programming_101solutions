def count_words(arr):
    result_dict = {}
    for each in arr:
        if each in result_dict.keys():
            result_dict[each] = result_dict[each] + 1
        else:
            result_dict[each] = 1
    return result_dict

def count_words2(words):
    return {key: words.count(key) for key in words}

def unique_words(words):
    return len([key for key in count_words(words)])

"""
print(count_words(["apple", "banana", "apple", "pie"]))
print(count_words(["python", "python", "python", "ruby"]))
"""


def unique_words_count(arr):
    return len(set(arr))
"""
print(unique_words_count(["apple", "banana", "apple", "pie"]))
print(unique_words_count(["python", "python", "python", "ruby"]))
print(unique_words_count(["HELLO!"] * 10))
"""


def nan_expand(times):
    if times == 0:
        return ""
    elif times == 1:
        return "Not a NaN"
    else:
        return "Not a " + nan_expand(times - 1)
"""
print(nan_expand(0))
print(nan_expand(1))
print(nan_expand(2))
print(nan_expand(3))
"""


def iterations_of_nan_expand(expanded):
    length = len(expanded)
    if length == 0:
        return 0
    elif (length - 9) % 6 == 0 and expanded == nan_expand((length - 9) // 6 + 1):
        return (length - 9) // 6 + 1
    else:
        return False
"""
print(iterations_of_nan_expand(""))
print(iterations_of_nan_expand("Not a NaN"))
print(iterations_of_nan_expand(
    'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print(iterations_of_nan_expand("Show these people!"))
"""


def prime_factorization(n):
    result_list = []
    for each in range(2, n + 1):
        current_counter = 0
        while n % each == 0:
            current_counter += 1
            n = n // each
        if current_counter != 0:
            result_list.append((each, current_counter))
    return result_list
"""
print(prime_factorization(10))
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(89))
print(prime_factorization(1000))
"""


def group(l):
    result = []
    i = 0
    while i < len(l):
        current_list = []
        current_list.append(l[i])
        i += 1
        while i < len(l) and l[i] == current_list[0]:
            current_list.append(l[i])
            i += 1
        result.append(current_list)
    return result
"""
print(group([1, 1, 1, 2, 3, 1, 1]))
print(group([1, 2, 1, 2, 3, 3]))
"""


def max_consecutive(items):
    return max([len(each) for each in group(items)])
"""
print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
"""


def groupby(func, seq):
    dict_res = {}
    for each in seq:
        current_list = []
        dict_res[func(each)] = current_list
    for each in dict_res.keys():
        for item in seq:
            if each == func(item):
                dict_res[each].append(item)
    return dict_res
"""
print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
print(groupby(lambda x: 'odd' if x %
              2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))
"""


def prepare_meal(number):
    result = ""
    counter = 0
    if number % 3 == 0:
        while number % 3 == 0:
            counter += 1
            number = number // 3
    for each in range(0, counter):
        result = result + "spam "

    if number % 5 == 0:
        if result == "":
            result = result + "eggs"
        else:
            result = result + "and eggs"
    return result
"""
print(prepare_meal(5))
print(prepare_meal(3))
print(prepare_meal(27))
print(prepare_meal(15))
print(prepare_meal(45))
print(prepare_meal(7))
"""


def reduce_file_path(path):
    tmp = path.split("/")
    for i in range(0, len(tmp)):
        if tmp[i] == ".":
            tmp.pop(i)
        elif tmp[i] == "..":
            tmp.pop(i)
            if i - 1 >= 0:
                tmp.pop(i - 1)
        else:
            pass
    return "/" + "/".join(tmp)

print(reduce_file_path("/"))
print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/www/htdocs/wtf/"))
print(reduce_file_path("/srv/www/htdocs/wtf"))
print(reduce_file_path("/srv/./././././"))
print(reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/etc/../etc/../etc/../"))
print(reduce_file_path("//////////////"))
print(reduce_file_path("/../"))


def is_an_bn(word):
    if word == "":
        return True
    else:
        tmp = group(word)
        return len(tmp) == 2 and len(tmp[0]) == len(tmp[1])  \
            and tmp[0][0] == 'a' and tmp[1][0] == 'b'
"""
print(is_an_bn(""))
print(is_an_bn("rado"))
print(is_an_bn("aaabb"))
print(is_an_bn("aaabbb"))
print(is_an_bn("aabbaabb"))
print(is_an_bn("bbbaaa"))
print(is_an_bn("aaaaabbbbb"))
"""


def magic_square(matrix):
    tmp = []
    dimensions = len(matrix)
    diag1, diag2 = 0, 0
    for row in matrix:
        tmp.append(sum(row))
    for i in range(0, dimensions):
        diag1 += matrix[i][i]
        diag2 += matrix[i][dimensions - 1 - i]
    tmp.append(diag1)
    tmp.append(diag2)
    for i in range(0, dimensions):
        sum_helper = 0
        for k in range(0, dimensions):
            sum_helper += matrix[k][i]
        tmp.append(sum_helper)
    return len(group(tmp)) == 1
"""
print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
print(
    magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
"""


def sum_of_divisors(n):
    return n + sum([each for each in range(1, n // 2 + 1) if n % each == 0])


def is_prime(n):
    return sum_of_divisors(n) == (1 + n)


def primes_to_n(n):
    return [each for each in range(0, n) if is_prime(each)]


def goldbach(n):
    return [(each, n - each) for each in range(0, n // 2 + 1) if is_prime(each) and is_prime(n - each)]

"""
print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))
"""


def odd(n):
    return n % 2 != 0


def to_digits(n):
    return [int(x) for x in str(n)]


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_number(digits):
    result = 0
    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit
    return result


def is_credit_card_valid(number):
    tmp = to_digits(number)[::-1]
    for i in range(1, len(tmp), 2):
        tmp[i] = tmp[i] * 2
    validation = to_number(tmp)
    return odd(len(tmp)) and sum(to_digits(validation)) % 10 == 0
"""
print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))
"""

def friday_years(start, end):
    years = []
    

    return len(years)