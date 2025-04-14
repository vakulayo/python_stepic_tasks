def paths_count(x, y):
    if x == 1 and y == 0: return 1
    elif x == 0 and y == 1: return 1
    elif x == 0: return paths_count(x, y-1)
    elif y == 0: return paths_count(x-1, y)
    else: return paths_count(x-1,y) + paths_count(x, y-1)

print(paths_count(2,2))