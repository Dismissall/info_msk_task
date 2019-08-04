quantity = int(input())
count_of_zero = 0
for x in range(1, quantity + 1):
    number = int(input())
    if number == 0:
        count_of_zero += 1
print(count_of_zero)
