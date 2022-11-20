"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from math import sqrt

def trianglemaker(p):
    lst = list()
    for a in range(1, p):
        for b in range(a, p):
            c2 = a ** 2 + b ** 2
            c = int(sqrt(c2))
            if sqrt(c2) == c and a+b+c<p:
                lst.append(a+b+c)

    max = 0
    lst2 = list()
    for i in lst:
        if lst.count(i) > max:
            max = lst.count(i)
            lst2.append(i)
    return lst2[-1]

print(trianglemaker(1000))