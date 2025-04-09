def add(a, b):
   # print(str(a) + ' ' + str(b) + ' ddddddddddddd')
    return a + b


def call(func, *args, **kwargs):
    if len(args) == 2: return func(args[0], args[1])
    elif len(args) == 1:
        return max(*args)
    else:
        #print(kwargs['a'])
        #print(kwargs['b'])
        return kwargs['a'] + kwargs['b']



print(call(add, 2, 3))
print(call(add, a = 4, b = 1))
print(call(max, [3,2,4,7]))




