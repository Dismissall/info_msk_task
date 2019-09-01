L = list(map(int, input().split()))

for x in range(len(L) - 1):
    if L[x] * L[x + 1] > 0:
        print(L[x], L[x + 1])
        break
