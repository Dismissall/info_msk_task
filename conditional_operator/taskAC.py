f_num = int(input())
s_num = int(input())
t_num = int(input())
if (f_num + s_num) % 2 != 0 or (f_num + t_num) % 2 != 0 or (s_num + t_num) % 2 != 0:
    print("YES")
else:
    print("NO")
