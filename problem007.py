"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

def is_prime(x):
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True
list1=list()
n=2
while True:
    if(is_prime(n)):
        list1.append(n)
    if(len(list1) == 10001):
        break
    n +=1
print(list1[-1])