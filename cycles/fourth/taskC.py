sum_of_num = 0
count = 0
while True:
    number = int(input())
    if number != 0:
        sum_of_num += number
        count += 1
    else:
        break
print(sum_of_num/count)
