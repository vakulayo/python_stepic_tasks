#task about decode line into file from 3.4
with open('input.txt', 'r') as file:
    line = file.readline().strip()

with open('output.txt', 'w') as file2:
    current_symbol = line[0]
    current_number = ''
    counter = 1
    for letter in line[1:]:
        counter += 1
        if letter.isalpha():
            file2.write(current_symbol * int(current_number))
            current_symbol = letter
            current_number = ''
        else:
            current_number += letter
            if counter == len(line): file2.write(current_symbol * int(current_number))
