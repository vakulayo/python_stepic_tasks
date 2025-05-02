def total_sum(filename):
    result = 0
    with open(filename) as file:
        for st in file:
            result += sum(map(float, st.split()))
    return result


print(total_sum('/home/ekaterina/Downloads/file1.txt'))


def minmax_coords(filename):
    all_x, all_y = [], []
    with open(filename) as file:
        for line in file:
            if line.splitlines() != ['']:
                all_x.append(int(line.split()[0]))
                all_y.append(int(line.split()[1]))
    return min(all_x, default=None), max(all_x, default=None), min(all_y, default=None), max(all_y, default=None)


print(minmax_coords('/home/ekaterina/Downloads/points1.txt'))
