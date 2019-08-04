from math import log2

number = int(input())
power = log2(number)
if power.is_integer():
    print(int(power))
else:
    print(int(power) + 1)
