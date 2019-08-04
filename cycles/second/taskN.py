quantity = int(input())
count_of_zero = 0
count_of_poz = 0
count_of_neg = 0
for x in range(1, quantity + 1):
    number = int(input())
    if number == 0:
        count_of_zero += 1
    elif number > 0:
        count_of_poz += 1
    else:
        count_of_neg += 1

print(count_of_zero, count_of_poz, count_of_neg)