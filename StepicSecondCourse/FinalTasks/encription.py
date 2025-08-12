# code_input = list(input())
# code_output = list(input())
#
# str_to_encode = input()
# str_to_decode = input()

code_input = list('abcd')
code_output = list('*d%#')

str_to_encode = 'abacabadaba'
str_to_decode = '#*%*d*%'

key_to_encode = {}
key_to_decode = {}

for i in range(len(code_input)):
    key_to_encode[code_input[i]] = code_output[i]
    key_to_decode[code_output[i]] = code_input[i]


def use_dictionary(line, dictionary):
    temp_list = list(line)
    for i in range(len(temp_list)):
        temp_list[i] = dictionary[temp_list[i]]
    return ''.join(temp_list)


print(use_dictionary(str_to_encode, key_to_encode))
print(use_dictionary(str_to_decode, key_to_decode))

