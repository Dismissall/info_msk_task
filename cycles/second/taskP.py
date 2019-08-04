first_arg = int(input())
second_arg = int(input())
third_arg = int(input())
free_cof = int(input())

for x in range(0, 1001):
    answer = first_arg * (x ** 3) + second_arg * (x ** 2) + third_arg * x + free_cof
    if answer == 0:
        print(x)

