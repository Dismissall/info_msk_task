start_dist = int(input())
end_dist = int(input())
count_days = 1

while start_dist < end_dist:
    start_dist *= 1.1
    count_days += 1
else:
    print(count_days)
