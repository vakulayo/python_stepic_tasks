# task from 3.4 ca;cu;ate average mark by every student and then average marks per subject
math, phis, russ = [], [], []
with open('input3.txt', 'r') as file:
    for line in file:
        data = line.strip().split(';')
        math.append(int(data[1]))
        phis.append(int(data[2]))
        russ.append(int(data[3]))
        with open('output3.txt', 'a') as result_file:
            result_file.write(str((int(data[1]) + int(data[2]) + int(data[3])) / 3) + '\n')
with open('output3.txt', 'a') as result_file:
    result_file.write(str(sum(math) / len(math)) + ' ' + str(sum(phis) / len(phis)) + ' ' + str(sum(russ) / len(russ)))
