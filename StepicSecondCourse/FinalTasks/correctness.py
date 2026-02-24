dictionary = [input().lower() for i in range(int(input()))]
num_line = int(input())
mistakes = []
for i in range(num_line):
    line = input().lower().split()
    for word in line:
        if not word in dictionary:
            if not word in mistakes:
                mistakes.append(word)
print(*mistakes, sep = '\n')


# dictionary = set(input().lower() for i in range(int(input())))
# #text = set(input().lower().split() for i in range(int(input())))
# text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
# print('\n'.join(text-dictionary))

