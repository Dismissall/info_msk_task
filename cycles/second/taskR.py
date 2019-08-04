first_arg = int(input())
second_arg = int(input())
third_arg = int(input())
free_cof = int(input())
exp_number = int(input())
count_answer = 0

for x in range(0, 1001):
    if x != exp_number:
        answer = (first_arg * (x ** 3) + second_arg * (x ** 2) + third_arg * x + free_cof) / (x - exp_number)
    else:
        continue
    if answer == 0:
        count_answer += 1
print(count_answer)
