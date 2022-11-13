"""Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

def listofdigits(x):
    list2 = [*str(x)]
    list1 = [int(i) for i in list2]
    return list1

def sumoffifthpowers(x):
    sum = 0
    for i in listofdigits(x):
        sum+=i**5
    return sum

listofnumbers = list()

for i in range(2,6 * 9**5 +1):
    if i == sumoffifthpowers(i):
        listofnumbers.append(i)

print(sum(listofnumbers))
