number = int(input())
count_div = 0
denominator = number ** (1 / 2)

if denominator.is_integer():
    denominator -= 1
    count_div += 1

for x in range(1, int(denominator + 1)):
    if number % x == 0:
        count_div += 2
print(count_div)
