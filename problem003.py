"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143"""

x = 600851475143


def is_prime(x):
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True


for i in range(2, x + 1):
    if is_prime(i) and x % i == 0:
        print(i)

