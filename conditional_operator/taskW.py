f_side = int(input())
s_side = int(input())
t_side = int(input())
if f_side + s_side > t_side and s_side + t_side > f_side and f_side + t_side > s_side:
    lst1 = [f_side, s_side, t_side]
    lst1 = sorted(lst1)
    f_side = lst1[2]
    s_side = lst1[1]
    t_side = lst1[0]

    if f_side ** 2 == (s_side ** 2 + t_side ** 2):
        print("right")
    elif f_side ** 2 > (s_side ** 2 + t_side ** 2):
        print("obtuse")
    else:
        print("acute")
else:
    print("impossible")
