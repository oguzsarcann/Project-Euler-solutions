"""
How many, not necessarily distinct, values of C(n,r)
 for 1<=n<=100, are greater than one-million?
"""
import math

lst = list()
for n in range(1,101):
    for r in range(0,n+1):
        if math.comb(n,r)>1000000:
            lst.append((n,r))
print(len(lst))