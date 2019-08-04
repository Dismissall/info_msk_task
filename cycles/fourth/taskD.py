count = 0
while True:
    number = int(input())
    if number == 0:
        break
    if number % 2 == 0:
        count += 1
print(count)
