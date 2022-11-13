"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included."""

def listofdigits(x):
    list2 = [*str(x)]
    list1 = [int(i) for i in list2]
    return list1
def factorial(x):
    n = 1
    for i in range(1,x+1):
        n*=i
    return n

def sumoffactorials(x):
    sum = 0
    for i in listofdigits(x):
        sum+=factorial(i)
    return sum

listofnumbers = list()

for i in range(2,factorial(9)*7):
    if i ==sumoffactorials(i):
        listofnumbers.append(i)

print(sum(listofnumbers))