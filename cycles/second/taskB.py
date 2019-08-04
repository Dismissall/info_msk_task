f_number = int(input())
s_number = int(input())
t_number = int(input())
fo_number = int(input())

for x in range(f_number, s_number + 1):
    if x % fo_number == t_number:
        print(x, end=" ")