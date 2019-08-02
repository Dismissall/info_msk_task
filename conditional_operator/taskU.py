f_number = int(input())
s_number = int(input())
t_number = int(input())

if f_number == s_number and s_number == t_number:
    print(3)
elif f_number == s_number or s_number == t_number or f_number == t_number:
    print(2)
else:
    print(0)
