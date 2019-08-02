x_bishop = int(input())
y_bishop = int(input())
x_cor = int(input())
y_cor = int(input())

if x_bishop - x_cor == y_bishop - y_cor or x_bishop - x_cor == -(y_bishop - y_cor):
    print("YES")
else:
    print("NO")
