L = list(map(int, input().split()))

L.sort(key=lambda x: not x)
[print(element) for element in L]
