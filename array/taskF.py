L = list(map(int, input().split()))
# count = 0
# for x in range(1, len(L) - 1):
#     if L[x - 1] < L[x] > L[x + 1]:
#         count += 1
# print(count)

print(len([y for x, y in enumerate(L[1:-1]) if L[x] < y > L[x + 2]]))
