number = int(input())
lst1 = []
while number >= 1:
    lst1.append(number % 10)
    number //= 10

lst1.sort()
print(lst1[0], lst1[-1])
