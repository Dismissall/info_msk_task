number = int(input())
prev = -1
sum_num = 0

while True:
    if number == prev == 0:
        break
    sum_num += number
    prev = number
    number = int(input())

print(sum_num)
