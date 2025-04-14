def concat(*strings, sep=' '):
    return sep.join(strings)


print(concat("a", "b", "c"))
print(concat("a", "b", "c", sep=':'))


def percent(share, *round_digits):
    return str(round(share * 100, *round_digits)) + '%'


print(percent(0.0123))
print(percent(0.0123, 0))
print(percent(0.0123, 1))
print(percent(0.0123, 10))


def header(string, level=1):
    if level < 1:
        level = 1
    elif level > 6:
        level = 6

    return '#' * level + ' ' + string


print(header("A"))
print(header("A", 0))
print(header("A", 3))
print(header("A", 1))
print(header("A", 10))


def inc(a):
    return a + 1


def f_map(func, l):
    return list(map(func, l))


print(f_map(inc, [1, 2, 3]))
print(f_map(inc, []))


def print_these(c, a=None,b=None):
   print(a, "is stored in a")
   print(b, "is stored in b")
   print(c, "is stored in c")

print_these(5)

a = [1,2,3]
b = [*a,4,5,6]
print(b)