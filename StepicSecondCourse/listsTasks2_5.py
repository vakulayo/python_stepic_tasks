# task_1 number of elem 2.5 part
students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(len(students))

# task_2 sum from line 2.5 part
line = "4 -1 9 3"
l = line.split()
result = 0
for elem in l:
    result += int(elem)
print(result)

# task_3 summing of neighbour 2.5 part
line = '1 3 5 6 10'
l_input = line.split()
result = []
if len(l_input) == 1:
    result = l_input
else:
    for i in range(len(l_input)):
        result.append(int(l_input[i - 1]) + int(l_input[(i + 1) % len(l_input)]))
print(*result)

# task_4 enter only numbers which is repeated 2.5 part
#line = '4 8 0 3 4 2 0 3'
#line = '10'
line = '1 1 2 2 3 3'
l_input = line.split()
l_input.sort()
result = []
for elem in l_input:
    if l_input.count(elem) > 1 and not elem in result:
        result.append(elem)
print(*result)