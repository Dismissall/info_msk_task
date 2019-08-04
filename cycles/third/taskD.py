number = int(input())

while number > 1:
    if number % 2 == 0:
        number //= 2
    else:
        print("NO")
        break
else:
    print("YES")
