def add(a, b):
    return a + b


def call(func, *args, **kwargs):
    return func(*args, **kwargs)


print(call(add, 2, 3))
print(call(add, a=4, b=1))
print(call(max, [3, 2, 4, 7]))


def first(*args, **kwargs):
    if len(args):
        return args[0]
    elif len(kwargs):
        return kwargs[min(kwargs.keys())]


print(first(0.0123))
print(first(1, 0.0123, 0))
print(first(a="Hi!", bb='dsfsdf', ac='fffffffffffff'))
print(first(1, 2, 3, ["a"], b="honey"))
print(first())
print(first({'asdf': 4}, {'frf': 3}, {'_3': 18}))