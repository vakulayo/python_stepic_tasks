# list from 1 to 2000
a = [i + 1 for i in range(2000)]
# print(a)

# list from 1 to 10000 div 3
b = [i for i in range(1, 10001) if i % 3 == 0]
# print(b)

# list from input
ssss = '3 4 5 2 4'
c = [int(i) for i in ssss.split(' ')]
print(c)

# list of squares of input and show position
sssss = '34 23 56 7 2'
f = {k: int(v)**2 for (k,v) in enumerate(sssss.split())}
print(f)


# list of string with string after :
s = '70:ztuebs 0:zdhkpq 54:jkyfmo 16:ducsvpq 85:ntsaw'
print([v for (k, v) in enumerate(s.replace(':', ' ').split(' ')) if k % 2 != 0])
print([x.split(':')[1] for x in s.split()])

# dict with key - numbers, values - strings
ss = '73:yjanlou 82:fsbohtg 58:xfuln 1:zshywk'
print({int(word.split(':')[0]): word.split(':')[1] for word in ss.split()})
