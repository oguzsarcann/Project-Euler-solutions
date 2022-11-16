"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

values = {}

file = open("words.txt","r")

names = file.read()

file.close()

names.upper()

names = names.replace('"','')

list1 = list(names.split(","))

list1.sort()

def valuesofletter(i):
    return ord(i)-64

def valueofaword(x):
    sum = 0
    for i in x:
        sum += valuesofletter(i)
    return sum

scorelist=list()
for i in list1:
    scorelist.append(valueofaword(i))

lst=list(zip(scorelist,list1))

listoftrianglenumbers = list()

i=1

while True:
    if int(i*(i+1)/2)>max(scorelist):
        listoftrianglenumbers.append(int(i * (i + 1) / 2))
        break
    else:
        listoftrianglenumbers.append(int(i*(i+1)/2))
    i+=1

number = 0

for i,j in lst:
    if i in listoftrianglenumbers:
        number+=1
print(number)