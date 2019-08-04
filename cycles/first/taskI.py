# Не могу предложить более быстрого решения. Время исполнения O(n)
num_row = int(input())
sum_fact = 1
fact = 1
for x in range(1, num_row + 1):
    fact *= x
    sum_fact += 1/fact
print(round(sum_fact, 5))
