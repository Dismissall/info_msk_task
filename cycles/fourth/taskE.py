num_max = 0
while True:
    number = int(input())
    if number == 0:
        break
    if number > num_max:
        num_max = number
print(num_max)