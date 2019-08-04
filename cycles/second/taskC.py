begin_num = int(input())
end_num = int(input())
first_num = int(begin_num ** (1 / 2))
second_num = int(end_num ** (1 / 2))
if first_num ** 2 < begin_num:
    first_num += 1
if second_num ** 2 <= end_num:
    second_num += 1
for x in range(first_num, second_num):
    print(x**2)
