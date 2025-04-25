def total_sum(filename):
    result = 0
    with open(filename) as file:
        for st in file:
            result += sum(map(float, st.split()))
    return result


print(total_sum('/home/ekaterina/Downloads/file1.txt'))
