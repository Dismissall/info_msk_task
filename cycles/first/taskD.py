number = int(input())
num_of_comb = int(input())
max_number = max(number - num_of_comb, num_of_comb)
min_number = min(number - num_of_comb, num_of_comb)
answer = 1
for x in range(max_number+1, number + 1):
    answer *= x
for x in range(1, min_number + 1):
    answer /= x
print(int(answer))
