# task dictionaries  from 3.2
def update_dictionary(my_dict, key, value):
    if key in my_dict.keys():
        my_dict.get(key).append(value)
    elif key * 2 in my_dict.keys():
        my_dict.get(key * 2).append(value)
    else:
        my_dict[key * 2] = [value]


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)  # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)  # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)  # {2: [-1, -2, -3]}

# task from 3.2 about war and piece
line = 'a aa abC aa ac abc bcd a'
book = line.split()
my_dict1 = {}
for word in book:
    word = word.lower()
    if word in my_dict1:
        my_dict1[word] += 1
    else:
        my_dict1[word] = 1

for key1, value1 in my_dict1.items():
    print(key1, value1)


# task from 3.2 calculation values and store the one was calculated already
def f(x):
    print('vizov funktsii')
    return x * x * x


number, my_dict2, all_numbers = int(input()), {}, []
for i in range(number):
    x = int(input())
    all_numbers.append(x)
    if x not in my_dict2:
        my_dict2[x] = f(x)

for n in all_numbers:
    print(my_dict2[n])
