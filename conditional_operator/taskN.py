f_cof = int(input())
s_cof = int(input())

if f_cof == 0:
    if s_cof != 0:
        print("NO")
    else:
        print("INF")
else:
    if -s_cof % f_cof != 0:
        print("NO")
    else:
        print(-s_cof // f_cof)
