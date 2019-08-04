number = input()
lst1 = number
count_of_zeros = 0
for x in number:
    if x == '0':
        count_of_zeros += 1
else:
    print(count_of_zeros)
