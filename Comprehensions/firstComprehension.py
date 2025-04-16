# list from 1 to 2000
a = [i + 1 for i in range(2000)]
# print(a)

# list from 1 to 10000 div 3
b = [i for i in range(1, 10001) if i % 3 == 0]
# print(b)

# list from input
ssss = '3 4 5 2 4'
c = [int(i) for i in ssss.split(' ')]
print(c)

# list of squares of input and show position
sssss = '34 23 56 7 2'
f = {k: int(v)**2 for (k,v) in enumerate(sssss.split())}
print(f)


# list of string with string after :
s = '70:ztuebs 0:zdhkpq 54:jkyfmo 16:ducsvpq 85:ntsaw'
print([v for (k, v) in enumerate(s.replace(':', ' ').split(' ')) if k % 2 != 0])
print([x.split(':')[1] for x in s.split()])

# dict with key - numbers, values - strings
ss = '73:yjanlou 82:fsbohtg 58:xfuln 1:zshywk'
print({int(word.split(':')[0]): word.split(':')[1] for word in ss.split()})
print({int(key): value for key, value in (b.split(':') for b in ss.split())})


# first input - number of numbers to input; print summing
#print(sum([int(input()) for s in range(int(input()))]))

#print with 1 string without symbol '\n' and make in with max 100 symbols
# 0123456789
# 1234567890
# 2345678901
# 3456789012
# 4567890123
# 5678901234
# 6789012345
# 7890123456
# 8901234567
# 9012345678

[print('0123456789'[i:] + '0123456789'[:i]) for i in range(10)]

# print all primes number before 1000 (by 1 string code less than 200 symbols)
import math; print(*[num for num in range(2, 1000) if all([num % i != 0 for i in range(2, int(math.sqrt(num))+1)])])
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997