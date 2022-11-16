values = {}

file = open("names.txt","r")

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
score = 0
for i in range(0,len(scorelist)):
    score+=(i+1)*(scorelist[i])

print(score)
