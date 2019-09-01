L = list(map(int, input().split()))

[print(L[x], end=" ") for x in range(len(L)) if L.count(L[x]) == 1]

# for x in range(len(L)):
#     if L.count(L[x]) == 1:
#         print(L[x], end=' ')
