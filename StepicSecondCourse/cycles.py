# number of stars
i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1

# summing until 0
number, sum = int(input()), 0
while number !=0:
    sum += number
    number = int(input())
print(sum)


# find min that can br divided on both a and b
#a, b = int(input()), int(input())
a, b = 15, 12
result, i = a * b, a * b
while i > a:
    i -= 1
    if i % a == 0 and i % b == 0: result = i
print(result)


# task for break and continue
while True:
    num = int(input())
    if num > 100: break
    if num < 10: continue
    print(num)


# task for multiply table part - 2.3
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
a, b, c, d = 4, 8, 6, 10
print(' ', end='\t')
for i in range(c, d + 1):
    print(i, end='\t')
print('')
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print('')

# task for mean in interval
# a, b, sum, num = int(input()), int(input()), 0, 0
a, b, sum, num = -3, 12, 0, 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum += i
        num += 1
print(sum / num)

# task about genome 2.4 part
# genome = input()
genome = 'acggtgttat'
if len(genome) == 0:
    print(0)
else:
    print(100 * (genome.upper().count('c'.upper()) + genome.upper().count('g'.upper())) / len(genome))

# task just slices 2.4 also
s = 'abcdefghijk'
print(s[3:6])
print(s[:6])
print(s[3:])
print(s[::-1])
print(s[-3:])
print(s[:-6])
print(s[-1:-10:-2])
#def abcdef defghijk kjihgfedcba ijk abcde kigec

# task string coding 2.4
# line = input()
line = 'abc'
result_line, i = '', 0
while i < len(line):
    symbol = line[i]
    number = 1
    if i == len(line) - 1:
        result_line += symbol + str(number)
        break
    i += 1
    while symbol == line[i]:
        number += 1
        i += 1
        if i == len(line): break
    result_line += symbol + str(number)
print(result_line)


# task string coding 2.4 second solution
line = 'aabbcccfdf'
result_line = ''
previous = line[0]
counter = 1
for letter in line[1:]:
    if letter == previous:
        counter += 1
        previous = letter
    else:
        result_line += previous + str(counter)
        counter = 1
        previous = letter
print(result_line + previous + str(counter))
