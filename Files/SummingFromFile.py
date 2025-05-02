# sum for all number from the file
# 1.0 2.4
# .1 9.12 .3 .2
# 112.3
# should be 125.42
def total_sum(filename):
    result = 0
    with open(filename) as file:
        for st in file:
            result += sum(map(float, st.split()))
    return result


print(total_sum('/home/ekaterina/Downloads/file1.txt'))


# return min and max x coord and min and max y coord
# 1 2
# 3 4
# -2 23
# 3 -1
# should be (-2, 3, -1, 23)
def minmax_coords(filename):
    all_x, all_y = [], []
    with open(filename) as file:
        for line in file:
            if line.splitlines() != ['']:
                all_x.append(int(line.split()[0]))
                all_y.append(int(line.split()[1]))
    return min(all_x, default=None), max(all_x, default=None), min(all_y, default=None), max(all_y, default=None)


print(minmax_coords('/home/ekaterina/Downloads/points1.txt'))


# collect ids of solved tasks and return statistics
# 1,2
# 1,4
# 1,3
# 2,1
# 2,2
# 2,3
# 2,4
# should be {1:3, 2:4}
def solved_tasks_without_repeat(filename):
    result = {}
    with open(filename) as file:
        for line in file:
            if line.splitlines() != ['']:
                student_id = int(line.split(',')[0])
                result[student_id] = result.get(student_id, 0) + 1
    return result


# collect ids of solved tasks and return statistics
# 1,2
# 1,4
# 1,3
# 1,3
# 2,1
# 2,2
# 2,3
# 2,4
# should be {1:3, 2:4}
print(solved_tasks_without_repeat('/home/ekaterina/Downloads/students_results.txt'))


def solved_tasks(filename):
    result = {}
    with open(filename) as file:
        for line in file:
            if line.splitlines() != ['']:
                student_id, task_id = map(int, line.strip().split(','))
                result[student_id] = result.get(student_id, set())
                result[student_id].add(task_id)
    return {k: len(v) for k, v in result.items()}


print(solved_tasks('/home/ekaterina/Downloads/students_results_with_repetition.txt'))


# collect numbers and variety for flovers and return mean length by variety name
# "sepal.length","sepal.width","petal.length","petal.width","variety"
# 5.1,3.5,1.4,.2,"Setosa"
# 4.9,3,1.4,.2,"Setosa"
# 4.7,3.2,1.3,.2,"Setosa"
# 4.6,3.1,1.5,.2,"Setosa"
# 5,3.6,1.4,.2,"Setosa"
# 5.4,3.9,1.7,.4,"Setosa"
# 4.6,3.4,1.4,.3,"Setosa"
# 5,3.4,1.5,.2,"Setosa"
# 4.4,2.9,1.4,.2,"Setosa"

def mean_petal(filename, variety):
    result = {}
    with open(filename) as file:
        file.readline()
        for line in file:
            numbers = line.rstrip().split(',')
            current_variety = numbers[4].replace('"', '')
            result[current_variety] = result.get(current_variety, []) + [numbers[2]]
    return sum(map(float, result[variety])) / len(result[variety])


print(mean_petal('/home/ekaterina/Downloads/flowers.txt', 'Setosa'))
