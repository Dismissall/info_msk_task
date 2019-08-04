first_num = int(input())
second_num = int(input())

while first_num != second_num:
    if first_num % 2 == 0 and first_num // 2 > second_num:
        first_num //= 2
        print(":2")
    else:
        first_num -= 1
        print("-1")
