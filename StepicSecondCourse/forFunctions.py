# task from 3.1 just piecewise function
# def my_function(x):
#     if x <= -2:
#         return 1 - (x + 2) ** 2
#     elif -2 < x <= 2:
#         return -x / 2
#     else:
#         return (x - 2) ** 2 + 1
#
#
# print(my_function(4.5))
# print(my_function(-4.5))
# print(my_function(1))


# task from 3.1 modify list
def modify_list(my_list):
    length, i = len(my_list), 0
    while i < length:
        elem = my_list[i]

        if elem % 2:
            my_list.remove(elem)
            length -= 1
        else:
            my_list[i] = elem // 2
            i+=1




lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]
modify_list(lst)
print(lst)  # [1]


#another try
def modify_list_1(l):
    l[:] = [i//2 for i in l if not i % 2]

lst = [1, 2, 3, 4, 5, 6, 7, 8]
modify_list_1(lst)
print(lst) # [1, 2, 3, 4]
