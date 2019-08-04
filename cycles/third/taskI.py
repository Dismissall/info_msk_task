num_of_Fib = int(input())
first_numFib = 0
second_numFib = 1
count = 2

while second_numFib < num_of_Fib:
    count += 1
    first_numFib, second_numFib = second_numFib, first_numFib + second_numFib
if second_numFib == num_of_Fib:
    print(count-1)
else:
    print(-1)
