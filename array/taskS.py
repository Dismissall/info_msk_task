L = list(map(int, input().split()))

sum_pair = sum(L[x + 1:].count(y) for x, y in enumerate(L))
print(sum_pair)

# sum_pair = 0
# for x in range(len(L)):
#     sum_pair += L[x + 1:].count(L[x])
# print(sum_pair)
