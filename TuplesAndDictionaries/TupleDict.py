def vector_sum(v1, v2):
    return tuple(v1[i] + v2[i] for i in range(len(v1)))


print(vector_sum((1, 5), (2, 3)))


def character_count(string):
    char_dict = dict()
    for s in string:
        if s in char_dict:
            char_dict[s] += 1
        else:
            char_dict[s] = 1
    return char_dict


print(character_count("asdfaa"))


def max_par(a, b, c):
    if a < 0: return -b / (2 * a), - b ** 2 / (4 * a) + c


print(max_par(-2, 1, 0))
print(max_par(2, 1, 0))
