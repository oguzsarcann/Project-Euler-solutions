from fractions import Fraction as frac

i = frac(3,2)
lst = [frac(3,2)]
count = 0
while True:
    i = 1 + 1/(1+i)
    lst.append(i)
    if len(str(i.numerator))>len(str(i.denominator)):
        count+=1

    if len(lst)==1000:
        break

print(count)