quantity = int(input())

for x in range(1, quantity + 1):
    number = int(input())
    if number == 0:
        print("YES")
        break
else:
    print("NO")
