# people who can both play the violin and speak german
str1 = 'Trista Macmaster, Gigi Wall'
str2 = 'Roselee Mayhan, Rosamond Boan, Malik Madore, Keena Kopf, Trista Macmaster, Cortez Mestas, Barbar Mease, Elease Knudson, Chas Nevius, Serafina Shemwell'

set1 = set(str1.split(', '))
set2 = set(str2.split(', '))
print(', '.join(set1.intersection(set2)))

# exam for spy
str3 = '8 11 12 23'
str4 = '23 12 11 11 23 12 8'

task = set(str3.split(' '))
answer = set(str4.split(' '))

if task == answer:
    print('YES')
else:
    print('NO')

# all children father and mother are remembered
str5 = 'Norma, Anja'
str6 = 'Alexandra, Roma, Jettie, Phung, Daron'

mother = set(str5.split(', '))
father = set(str6.split(', '))
print(', '.join(mother.union(father)))

# number of children parents are forget
number_of_children = 11
str7 = 'Anja, Tom, Alexandra, Roma'
str8 = 'Phung'

mother = set(str7.split(', '))
father = set(str8.split(', '))
print(number_of_children - len(mother.union(father)))



#violinist can't speak german
violin = set(str1.split(', '))
german = set(str2.split(', '))
print(', '.join(violin.difference(german)))


#people who can do only one thing
print(*violin.symmetric_difference(german), sep=', ')
