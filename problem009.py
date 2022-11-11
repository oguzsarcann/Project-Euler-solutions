"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
listofpythagoreantriples=list()

def ispythagorean(x,y,z):
    if x**2 +y**2 == z**2:
        return True
    return False
for a in range(1,1000):
    for b in range(a,1000):
        for c in range(b,1000):
            if ispythagorean(a,b,c):
                if a+b+c == 1000:
                    print(a*b*c)

"""
Also:

import math

n =1000
list1=([(a, b, int(c)) for a in range(1, n + 1) for b in range(a, n + 1)
       if (c := math.sqrt(a**2 + b**2)) % 1 == 0 and c <= n])

for (i,j,k) in list1:
    if(i +j +k == 1000):
        print(i*j*k)
"""