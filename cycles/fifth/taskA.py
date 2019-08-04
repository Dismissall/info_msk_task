number = int(input())
sum_of_num = 0
while number >= 1:
    sum_of_num += number % 10
    number //= 10
else:
    print(sum_of_num)
