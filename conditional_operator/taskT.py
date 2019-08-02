f_side = int(input())
s_side = int(input())
t_side = int(input())

if f_side + s_side > t_side and s_side + t_side > f_side and f_side + t_side > s_side:
    print("YES")
else:
    print("NO")
