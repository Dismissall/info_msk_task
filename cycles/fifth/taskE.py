number = int(input())
lst1 = []
while 0 < number:
    lst1.append(number % 10)
    number //= 10
for x in lst1: print(x, end="")
