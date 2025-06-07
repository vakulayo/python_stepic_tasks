def transpose(initial_list):
    result_list = [[i for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            result_list[j][i] = initial_list[i][j]
    return result_list


inp = [
    [None, 0, 1],
    [None, None, None],
    [1, 0, 1]
]

print(transpose(inp))
