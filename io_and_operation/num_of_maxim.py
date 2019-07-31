first_num = int(input())
second_num = int(input())
answer = (first_num // second_num * first_num + second_num // first_num * second_num) / (
        first_num // second_num + second_num // first_num)
print(int(answer))
