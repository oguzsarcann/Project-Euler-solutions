"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10  without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

def list_of_divisors(x):
    list1=list()
    for i in range(1,x+1):
        if(x%i==0):
            list1.append(i)
    return list1
def common_members(x,y):
    result=[i for i in x if i in y ]
    return result
def leastcommonmultiple(x,y):
    return int(x*y/common_members(list_of_divisors(x),list_of_divisors(y))[-1])

listofnumbers=list(range(1,21))
number = 1
for i in listofnumbers:
    number=leastcommonmultiple(number,i)
print(number)

"""There is also lcm() function in math module:
lcm(*integers)
    Least Common Multiple.
----------------
import math
print(math.lcm(*range(1,21)))---->  232792560

"""