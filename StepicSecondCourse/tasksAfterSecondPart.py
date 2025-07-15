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


# task_4

# task_5 print spiral matrix from 2.6
# n = int(input())
n = 6
matrix = [[0 for ii in range(n)] for jj in range(n)]
if n == 1:
    matrix[0][0] = 1
else:
    i, j = 0, 0
    direction = 0
    for k in range(1, n * n + 1):
        matrix[i][j] = k
        #check if we reached a border, if yes - change the direction
        if ((direction % 4 == 0 and j == n - 1) or (direction % 4 == 1 and i == n - 1) or
                (direction % 4 == 2 and j == 0) or (direction % 4 == 3 and i == 0)):
            direction += 1
        #check we reached a non-zero value already, need to change the direction
        if ((direction % 4 == 0 and matrix[i][j + 1] != 0) or (direction % 4 == 1 and matrix[i + 1][j] != 0) or
                (direction % 4 == 2 and matrix[i][j - 1]) or (direction % 4 == 3 and matrix[i - 1][j] != 0)):
            direction += 1

        if direction % 4 == 0:
            j += 1
        elif direction % 4 == 1:
            i += 1
        elif direction % 4 == 2:
            j -= 1
        else:
            i -= 1

for line in matrix:
    print(*line)
