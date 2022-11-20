"""Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of
an integer with (1,2, ... , n) where n > 1?"""

def ispandigital(x):
    lst = list(range(1,10))
    lst2 = [int(i) for i in list(str(x))]
    lst2.sort()
    if lst2==lst:
        return True
    return False

def pantigitalmaker(x):
    str1=""
    i=1
    while True:
        if len(str1)>=9:
            break
        else:
            str1+=str(i*x)
            i+=1

    if ispandigital(int(str1)):
        return int(str1)
    else:
        return 0

listofpandigitals=list()
for i in range(1,10000):
    if pantigitalmaker(i)!=0:
        listofpandigitals.append(pantigitalmaker(i))

listofpandigitals.sort()
print(listofpandigitals)
