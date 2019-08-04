num_of_Fib = int(input())
first_numFib = 0
second_numFib = 1
count = 2
if num_of_Fib < 2:
    print(num_of_Fib)
else:
    while count < num_of_Fib + 1:
        count += 1
        first_numFib, second_numFib = second_numFib, first_numFib + second_numFib
    else:
        print(second_numFib)
