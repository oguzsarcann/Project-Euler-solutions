"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?"""

import sympy

i = 1
primes = list()

while True:
    if sympy.isprime(i):
        if sum(primes) + i >1000000:
            break
        primes.append(i)
    i+=1

length=0
prime=0

for i in range(0,len(primes)):
    for j in range(i,len(primes)+1):
        if sympy.isprime((sum(primes[i:j]))):
            if j-i>length:
                length=j-i
                prime=sum(primes[i:j])

print(length)
print(prime)