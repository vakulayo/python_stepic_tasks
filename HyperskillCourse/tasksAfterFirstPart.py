# task_1: triangle square
a, b, c = int(input()), int(input()), int(input())
p = (a + b + c) / 2
square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(square)

# task_2: in number in (−15,12]∪(14,17)∪[19,+∞)
n = int(input())
if (-15 < n <= 12) or (14 < n < 17) or (n >= 19):
    print(True)
else:
    print(False)

# task_3: simple calc +, -, /, *, mod, pow, div,
first, second = float(input()), float(input())
operator = input()
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "/":
    if second != 0:
        print(first / second)
    else:
        print("Деление на 0!")
elif operator == "*":
    print(first * second)
elif operator == "mod":
    if second != 0:
        print(first % second)
    else:
        print("Деление на 0!")
elif operator == "pow":
    print(first ** second)
elif operator == "div":
    if second != 0:
        print(first // second)
    else:
        print("Деление на 0!")


# task_4: figure square
figure_type = input()
if figure_type == "треугольник":
    a, b, c =  float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif figure_type == "прямоугольник":
    a, b = float(input()), float(input())
    print(a * b)
elif figure_type == "круг":
    r = float(input())
    print(3.14 * r**2)
else:
    print("Wrong figure type")

# task_5: sort 3 number by max, min, left
a, b, c = int(input()), int(input()), int(input())
if a > b: a, b = b, a
if b > c: b, c = c, b
if a > b: a, b = b, a
print(str(c) + '\n' + str(a) + '\n' + str(b))
