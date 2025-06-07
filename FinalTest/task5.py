def check_diagonal(arr, digit):
    result = False
    if arr[0][0] == arr[1][1] == arr[2][2] == digit: result = True
    return result

# arr = [
#     [1, None, 0],
#     [0, 1,    0],
#     [1, None, 1]
# ]
# digit = 1



# print(check_diagonal(arr, digit))