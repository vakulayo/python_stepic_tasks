# list from 1 to 2000
a = [i + 1 for i in range(2000)]
print(a)

# list from 1 to 10000 div 3
b = [i for i in range(1, 10001) if i % 3 == 0]
print(b)

# list from input
c = [int(i) for i in input().split(' ')]
print(c)


# list of squares of input and show position
f = {k: int(v)**2 for (k,v) in enumerate(input().split())}
print(f)