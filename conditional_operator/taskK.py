from math import fabs

x_knight = int(input())
y_knight = int(input())
x_cor = int(input())
y_cor = int(input())

if fabs(x_knight - x_cor) == 1 and fabs(y_knight - y_cor) == 2:
    print("YES")
elif fabs(x_knight - x_cor) == 2 and fabs(y_knight - y_cor) == 1:
    print("YES")
else:
    print("NO")
