number = int(input())
first_part = number // 100
second_part = number % 100
second_part = second_part % 10 * 10 + second_part // 10
print(second_part - first_part + 1)
