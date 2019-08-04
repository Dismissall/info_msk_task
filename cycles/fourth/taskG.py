first_num_max = second_num_max = 0
number = int(input())
while number != 0:
    if number > first_num_max:
        first_num_max, second_num_max = number, first_num_max
    if second_num_max < number < first_num_max:
        second_num_max = number
    number = int(input())
else:
    print(second_num_max)
