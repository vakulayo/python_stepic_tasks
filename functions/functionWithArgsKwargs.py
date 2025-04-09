def add(a, b):
    return a + b


def call(func, *args, **kwargs):
    return func(*args, **kwargs)

print(call(add, 2, 3))
print(call(add, a=4, b=1))
print(call(max, [3, 2, 4, 7]))
