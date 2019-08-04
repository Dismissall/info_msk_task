number = int(input())
prev_num = 0
count = -1
while number != 0:
    if number > prev_num:
        count += 1
    prev_num = number
    number = int(input())
print(count)
