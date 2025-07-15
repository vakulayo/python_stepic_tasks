# task_1 from 2.6 summ of square when sum of number is 0
result = num = int(input())
summ = num*num
while result != 0:
    current = int(input())
    result+=current
    summ += current*current
print(summ)

# task_2 from 2.6 print increment number each time equal times until whole number is reached
desired_num, current_num = 10, 0
for i in range(1, desired_num + 1):
    if current_num == desired_num: break
    for j in range(1, i + 1):
        print(i, end=' ')
        current_num += 1
        if current_num == desired_num: break
print()


# another try
desired_num, num_list, i = 15, [], 1
while len(num_list) < desired_num:
    num_list += [i] * i
    i += 1
print(*num_list[:desired_num])

# task_3 from 2.6
line = '5 8 2 7 8 8 2 4'
number = 8
positions = []
num_list = [int(i) for i in line.split()]
for j in range(len(num_list)):
    if num_list[j] == number:  positions.append(j)
if len(positions) > 0:
    print(*positions)
else:
    print('Отсутствует')
