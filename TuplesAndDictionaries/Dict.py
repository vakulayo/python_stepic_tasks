def code_number(num):
    return ' '.join({'0': "zero",
                     '1': "one",
                     '2': "two",
                     '3': "three",
                     '4': "four",
                     '5': "five",
                     '6': "six",
                     '7': "seven",
                     '8': "eight",
                     '9': "nine"}.get(digit) for digit in str(num))


print(code_number(230))  # == "two three zero"


def average_attempts(attempts, names):
    dict_temp = {}
    for user_id, task, attempt in attempts:
        dict_temp[user_id] = (dict_temp.get(user_id, (0, 0))[0] + 1, dict_temp.get(user_id, (0, 0))[1] + attempt)

    final_dict = {}
    for user_id, name in names:
        if dict_temp.get(user_id):
            final_dict[name] = dict_temp[user_id][1] / dict_temp[user_id][0]

    return final_dict


attempts = [(1232323323415, 1, 43),
            (1232323323415, 2, 3),
            (114349, 1, 0)
            ]
names = [(114349, "Arkady"),
         (114348, "ArkadyJunior"),
         (1232323323415, "Random")]

print(average_attempts(attempts, names))  # == {'Random': 23.0, 'Arkady': 0.0}
