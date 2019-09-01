L = list(map(int, input().split()))

for i in range(0, len(L) - 1, 2):
    L[i], L[i + 1] = L[i + 1], L[i]

[print(element, end=" ") for element in L]
