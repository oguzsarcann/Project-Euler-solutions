"""The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""

def numberofdigits(x):
    return len(str(x))
lst=list()
for i in range(1,10):
    j=1
    while True:
        if j == numberofdigits(i**j):
            lst.append(i**j)
        else:
            break
        j+=1

lst.sort()
print(lst)
print(len(lst))