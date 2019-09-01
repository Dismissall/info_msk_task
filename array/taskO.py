L = list(map(int, input().split()))

element = L.pop()
L.insert(0, element)

[print(x) for x in L]
