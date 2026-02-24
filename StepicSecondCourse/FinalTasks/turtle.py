steps = int(input())
x, y = 0, 0
for i in range(steps):
    command = input().split()
    if command[0] == 'север': y+=int(command[1])
    elif command[0] == 'юг': y-=int(command[1])
    elif command[0] == 'запад': x-=int(command[1])
    elif command[0] == 'восток': x+=int(command[1])
print(x, y)














