#task about collect text from file and count words. Return most frequent word
my_dict = dict()
max_count = 1
with open('input1.txt', 'r') as file:
    for line in file:
        words = line.lower().split()
        for word in words:
            my_dict[word] =  my_dict.get(word, 0) + 1
            if my_dict[word] > max_count: max_count = my_dict[word]


result = set()
for key, value in my_dict.items():
    if value == max_count:
        result.add(key)
print(max(result), max_count)