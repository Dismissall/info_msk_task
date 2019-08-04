num_of_sec = int(input())
step = 1
while num_of_sec > 0:
    count = step
    if step > num_of_sec:
        count = num_of_sec
    for x in range(1, count+1):
        print(step, end=" ")
    num_of_sec -= step
    step += 1

