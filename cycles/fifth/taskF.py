number = int(input())
sum_count = 0
while number > 0:
    string_num = str(number)
    if string_num == string_num[::-1]:
        sum_count += 1
    number -= 1
else:
    print(sum_count)
