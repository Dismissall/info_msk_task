f_number = int(input())
s_number = int(input())
# lst = []
for x in range(f_number, s_number + 1):
    if x % 2 == 0:
        print(x, end=" ")