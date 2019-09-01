L = list(map(int, input().split()))

# for x in range(1, len(L)):
#     if L[x - 1] < L[x]:
#         print(L[x], end=' ')

[print(y, end=" ") for x, y in enumerate(L[1:]) if y > L[x]]
