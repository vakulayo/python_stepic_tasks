#!/usr/bin/env python
from copy import deepcopy

initial_state = [['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
 ['#', '#', '#', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
n = int(input())

for s in range(10):
    initial_state[s] = ['.'] + initial_state[s] + ['.']
add_dead_frame = [12 * ['.']] + initial_state + [12 * ['.']]

def live_number(ik, jk, li):
    sum = 0
    if li[ik - 1][jk - 1] == '#': sum += 1
    if li[ik - 1][jk] == '#': sum += 1
    if li[ik - 1][jk + 1] == '#': sum += 1
    if li[ik][jk - 1] == '#': sum += 1
    if li[ik][jk + 1] == '#': sum += 1
    if li[ik + 1][jk - 1] == '#': sum += 1
    if li[ik + 1][jk] == '#': sum += 1
    if li[ik + 1][jk + 1] == '#': sum += 1
    return sum


result = deepcopy(add_dead_frame)

for k in range(n):
    add_dead_frame=deepcopy(result)
    for i in range(1, 10):
        for j in range(1, 10):
            number = live_number(i, j, add_dead_frame)
            if add_dead_frame[i][j] == '.' and number == 3:
                result[i][j] = '#'
            if add_dead_frame[i][j] == '#' and number in [0, 1, 4, 5, 6, 7, 8]:
                result[i][j] = '.'
result.pop(0)
result.pop(10)
for s in range(10):
    result[s].pop(0)
    result[s].pop(10)
print(*result, sep='\n')
