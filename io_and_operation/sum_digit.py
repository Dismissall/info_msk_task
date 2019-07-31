number = int(input())
num_sum = 0
while number > 0:
    num_sum += number % 10
    number = number // 10
print(num_sum)
