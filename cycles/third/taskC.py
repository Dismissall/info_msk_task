from math import log2

number = int(input())
power = int(log2(number))
count = 0
while count <= power:
    print(2 ** count, end=" ")
    count += 1
