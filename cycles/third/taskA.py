number = int(input())
num_pow = 1
while num_pow ** 2 <= number:
    print(num_pow ** 2)
    num_pow += 1
