def fix_duplicates(ids):
    dict_temp, position = {}, 0

    for elem in ids:
        if dict_temp.get(elem):
            dict_temp[elem] = dict_temp.get(elem) + 1
        else:
            dict_temp[elem] = 1
        if dict_temp[elem] > 1: ids[position] = elem + '_' + str(dict_temp[elem] - 1)
        position += 1
    return ids


ids = ["a", "b", "c", "a", "a", "d", "c"]
print(fix_duplicates(ids))  # == ['a', 'b', 'c', 'a_1', 'a_2', 'd', 'c_1']


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def calc(a, op, b):
    return {'+': add,
            '/': div,
            '*': mul,
            '-': sub}.get(op)(a,b)


print(calc(2, '+', 4))  # == 6
print(calc(3, "/", 2))  # == 1.5
print(calc(3, '*', 13))  # == 39
print(calc(4, "-", 3))  # == 1
