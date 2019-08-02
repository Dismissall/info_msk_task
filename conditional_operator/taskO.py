f_cof = int(input())
s_cof = int(input())
t_cof = int(input())
four_cof = int(input())
x_answer = 0

if f_cof == 0:
    if s_cof != 0:
        print("NO")
    else:
        print("INF")
else:
    if -s_cof % f_cof != 0:
        print("NO")
    else:
        x_answer = -s_cof // f_cof

        if t_cof * x_answer + four_cof == 0:
            print("NO")
        else:
            print(x_answer)
