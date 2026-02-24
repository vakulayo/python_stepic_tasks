result = {}
with open('input.txt', 'r') as file:
    for line in file:
        l = line.strip().split()
        result[int(l[0])] = result.get(int(l[0]), []) + [int(l[2])]



for k in range(1, 12):
    if k not in result: print(k, '-')
    else: print(k, sum(result[k])/len(result[k]))
