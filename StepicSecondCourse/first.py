#a lot of print examples
print(*range(1, 11))
print(10)
print("Supercalifragilisticexpialidocious")
code2 = 'Python\'s core and more'
print(code2)
code3 = "Python's core and more"
print(code3)

print(2014 ** 14)
print(1.2345e-3)

print(2014.0 ** 14)
print(7 / 3)
print(7 // 3)
print(int(2.99))
print(int(-1.6))
print(9 ** 19 - int(float(9 ** 19)))
print(float(9 ** 19))
print(int(float(9 ** 19)))
print(9 ** 19)

print(type(7.0))

x = int(input())
print(x // 60)
print(x % 60)

#alarm clock
xx, h, m = int(input()), int(input()), int(input())
if (xx % 60 + m) >= 60:
    print(xx // 60 + h + 1)
    print(xx % 60 + m - 60)
else:
    print(xx // 60 + h)
    print(xx % 60 + m)

#correct brackets
a, b = True, False
print((a and b) or ((not a) and (not b)))

x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)

a = True
b = False
print((a and b) or (not a and not b))


# leap year
n = int(input())
if (n % 400 == 0) or (n % 100 != 0 and n % 4 == 0):
    print("Високосный")
else:
    print("Обычный")
