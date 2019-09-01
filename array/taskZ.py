L = list(map(int, input().split()))
shift = int(input())

# [print(x, end=" ") for x in L[-shift::1]]
# [print(x, end=" ") for x in L[:-shift:1]]

for x in range(len(L)):
    print(L[(x - shift + len(L)) % len(L)], end=" ")
