"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""

def isprime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def numberofdigits(x):
    return len(str(x))

def anyevendigit(x): #if there is a even number, then at least one of the rotations cannot be a prime number except the number 2
    if "0" in str(x) or "2" in str(x) or "4" in str(x) or "6" in str(x) or "8" in str(x):
        return True
    else:
        return False

def rotate(x):
    return int(x%(10**(numberofdigits(x)-1)))*10+int(x/10**(numberofdigits(x)-1))

def allrotations(x):
    list1=list()
    for i in range(0, numberofdigits(x)):
        list1.append(rotate(x))
        x = rotate(x)
    return list1

def isallrotationsprime(x):
    for i in allrotations(x):
        if not isprime(i) :
            return False
    return True

listofcircularprimes = [2]

for i in range(3,1000000):
    if anyevendigit(i):
        pass
    else:
        if isprime(i):
             if isallrotationsprime(i):
                 print(i)
                 listofcircularprimes.append(i)

print(len(listofcircularprimes))