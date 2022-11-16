"""
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""
def digital_sum(x):
    sum = 0
    for i in list((str(x))):
        sum += int(i)
    return sum

lst = list()

for a in range(1,100):
    for b in range(1,100):
        lst.append(digital_sum(a**b))

print(max(lst))
