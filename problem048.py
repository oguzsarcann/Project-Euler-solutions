"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
"""
number = 0
for i in range(1,1000):
    number+=i**i

print(number%10000000000)