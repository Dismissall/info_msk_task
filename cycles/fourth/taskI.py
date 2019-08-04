num_max = 0
count = 1
number = int(input())
while number != 0:
    if number == num_max:
        count += 1
    if number > num_max:
        num_max = number
        count = 1
    number = int(input())
else:
    print(count)
