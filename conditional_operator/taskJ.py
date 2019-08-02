from math import fabs

x_king = int(input())
y_king = int(input())
x_cor = int(input())
y_cor = int(input())

if fabs(x_king - x_cor) <= 1 and fabs(y_king - y_cor) <= 1:
    print("YES")
else:
    print("NO")
