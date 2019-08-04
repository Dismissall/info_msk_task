number = int(input())
prev = -1
count = 1
max_count = 1
while number != 0:
    if number != prev:
        prev = number
        count = 1
    else:
        count += 1
        if count > max_count:
            max_count = count
    number = int(input())
print(max_count)
