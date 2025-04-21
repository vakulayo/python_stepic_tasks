#number of lines in a file
f = open('/home/ekaterina/Downloads/file.txt', 'r')
counter = 0
for string in f:
    counter+=1
f.close()
print(counter)

#number of chars in a file
f2 = open('/home/ekaterina/Downloads/file.txt', 'r')
counter2 = 0
for st in f2:
    counter2+=len(st)
f2.close()
print(counter2)


#sum of numbers from file
def sum_numbers(filename):
    counter1 = 0
    with open(filename, 'r') as f1:
        for st1 in f1:
            counter1+=int(st1)
    return counter1

print(sum_numbers('/home/ekaterina/Downloads/file.txt'))


#add message to file
def write_message(filename, message):
    with open(filename, 'w') as f3:
        f3.write(message)
    pass

write_message('/home/ekaterina/Downloads/file.txt', 'I hate Trump')

#append message to file
def log(filename, message):
    with open(filename, 'a') as file:
        file.write(message + '\n')
    pass

log('/home/ekaterina/Downloads/file.txt', 'I hate Mask too')
log('/home/ekaterina/Downloads/file.txt', 'I hate Putin most of all')