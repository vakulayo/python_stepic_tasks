# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

num = int(input())
table = {}

def add_match(result_table, team_name, result):
    updated_res = result_table.get(team_name, [0, 0, 0, 0, 0])
    updated_res[0] += 1
    if result == 'win':
        updated_res[1] += 1
    elif result == 'defeat':
        updated_res[3] += 1
    else:
        updated_res[2] += 1
    result_table[team_name] = updated_res
    return result_table

for i in range(num):
    match = input().split(';')
    if int(match[1]) > int(match[3]):
        add_match(table, match[0], 'win')
        add_match(table, match[2], 'defeat')
    elif int(match[1]) < int(match[3]):
        add_match(table, match[0], 'defeat')
        add_match(table, match[2], 'win')
    else:
        add_match(table, match[0], 'draw')
        add_match(table, match[2], 'draw')

for key, value in table.items():
    value[4] = 3*value[1] + 1*value[2]
    table[key] = value
    print((key + ':'), *value, end='\n')


# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6