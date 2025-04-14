str1 = 'Trista Macmaster, Gigi Wall'
str2 = 'Roselee Mayhan, Rosamond Boan, Malik Madore, Keena Kopf, Trista Macmaster, Cortez Mestas, Barbar Mease, Elease Knudson, Chas Nevius, Serafina Shemwell'

set1 = set(str1.split(', '))
set2 = set(str2.split(', '))
print(', '.join(set1.intersection(set2)))

str3 = '8 11 12 23'
str4 = '23 12 11 11 23 12 8'

task = set(str3.split(' '))
answer = set(str4.split(' '))

if task == answer:
    print('YES')
else:
    print('NO')



