"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""
from math import gcd
listoffractions=list()
listofanswers = list()
for i in range(10,100):
    for j in range(i+1,100):
        listoffractions.append((i,j))

def func(x,y):
    if x%10==0 or y%10==0:
        return False
    else:
        if(x%10)==(y%10):
            if x/y == (x//10)/(y//10):
                return True
        elif (x//10)==(y%10):
            if x/y == (x%10)/(y//10):
                return True
        elif (x % 10) == (y // 10):
            if x / y == (x // 10) / (y % 10):
                return True
        elif x // 10 == y // 10:
            if x / y == (x % 10) / (y % 10):
                return True
        else:
            return False

for i,j in listoffractions:
    if func(i,j):
        listofanswers.append((i,j))
numerator=1
denomirator=1
for i,j in listofanswers:
    numerator*=i
    denomirator*=j

print(int(denomirator/gcd(numerator,denomirator)))







