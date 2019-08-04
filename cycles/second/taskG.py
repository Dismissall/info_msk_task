number = int(input())
min_div = number

for x in range(2, number + 1):
    if number % x == 0:
        min_div = x
        break
print(min_div)
