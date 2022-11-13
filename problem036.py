"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""

def ispalindromicbase10(x):
    if [*str(x)] == [*str(x)][::-1]:
        return True
    else:
        return False

def ispalindromicbase2(x):
    if [*bin(x)][2:] == [*bin(x)][-1:1:-1]:
        return True
    else:
        return False

listofnumbers = list()
for i in range(1,1000000):
    if(ispalindromicbase2(i) and ispalindromicbase10(i)):
        listofnumbers.append(i)
print(sum(listofnumbers))
