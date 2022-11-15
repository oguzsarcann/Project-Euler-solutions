"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations


def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


listofallpandigitalnumbers = list()
listofallpandigitalprimes = list()
for i in [4,7]:#other n-digit pantigital numbers cannot be prime because they are divisible by 3
    list1 = list(permutations(list(range(1, i + 1))))
    for j in list1:
        number = 0
        for k in j:
            number *= 10
            number += k
        if number%2!=0:
            listofallpandigitalnumbers.append(number)
for i in listofallpandigitalnumbers:
    if isprime(i):
        listofallpandigitalprimes.append(i)
print(max(listofallpandigitalprimes))
