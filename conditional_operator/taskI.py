from math import fabs

x_queen = int(input())
y_queen = int(input())
x_cor = int(input())
y_cor = int(input())

if fabs(x_queen - x_cor) == fabs(y_queen - y_cor):
    print("YES")
elif x_queen == x_cor or y_queen == y_cor:
    print("YES")
else:
    print("NO")
