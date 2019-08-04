number = int(input())
end_div = number // 2 if number % 2 == 0 else (number - 1) // 2
for x in range(1, end_div + 1):
    if number % x == 0:
        print(x)
print(number)
