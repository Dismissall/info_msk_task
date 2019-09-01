L = list(map(int, input().split()))

# 1-ыцй вариант: через filter
countPos = len(list(filter(lambda element: element > 0, L)))
print(countPos)

# 2-ой варинат: через enumerate
# countPos = len([1 for x, y in enumerate(L) if y > 0])
# print(countPos)
