def transpose(initial_list):
    result_list = [[i for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            result_list[j][i] = initial_list[i][j]
    return result_list


def check_column(arr, digit):
    result = False
    if arr[0][0] == arr[1][0] == arr[2][0] == digit: result = True
    if arr[0][1] == arr[1][1] == arr[2][1] == digit: result = True
    if arr[0][2] == arr[1][2] == arr[2][2] == digit: result = True
    return result


def check_line(arr, digit):
    return check_column(transpose(arr), digit)


input_list = [
    [None, None, 1],
    [0, None, 0],
    [1, None, 1]
]
digit = 1
print(check_column(input_list, digit))
print(check_line(input_list, digit))
input_list_2 = [
    [0, None, 1],
    [0, None, 0],
    [0, None, 1]
]
digit_2 = 0
print(check_column(input_list_2, digit_2))
print(check_line(input_list_2, digit_2))
