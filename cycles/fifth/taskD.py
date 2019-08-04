number = int(input())
lst1 = []
while number > 0:
    lst1.append(number % 2)
    number //= 2
for x in lst1: print(x, end="")
