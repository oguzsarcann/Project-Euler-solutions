"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

decimalfraction  = "0."
i=1
while True:
    decimalfraction +=str(i)
    i+=1
    if len(decimalfraction)>1000002:
        break

decimalfraction = decimalfraction[1:]
answer = 1
for i in range(0,7):
    answer*=int(decimalfraction[10**i])
print(answer)