number = int(input())
denominator = 2
while True:
    if number % denominator == 0:
        break
    else:
        denominator += 1
print(denominator)