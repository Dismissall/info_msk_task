L = list(map(int, input().split()))
min_num = min(filter(lambda element: element > 0, L))
print(min_num)
