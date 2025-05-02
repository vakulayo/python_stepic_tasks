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


def solved_tasks_without_repeat(filename):
    result = {}
    with open(filename) as file:
        for line in file:
            if line.splitlines() != ['']:
                student_id = int(line.split(',')[0])
                result[student_id] = result.get(student_id, 0) + 1
    return result


print(solved_tasks_without_repeat('/home/ekaterina/Downloads/sudentsresults.txt'))


def solved_tasks(filename):
    result = {}
    with open(filename) as file:
        for line in file:
            if line.splitlines() != ['']:
                student_id, task_id = map(int, line.strip().split(','))
                result[student_id] = result.get(student_id, set())
                result[student_id].add(task_id)
    return {k: len(v) for k, v in result.items()}

print(solved_tasks('/home/ekaterina/Downloads/sudents_results_with_repetition.txt'))
