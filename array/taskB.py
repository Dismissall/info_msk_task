L = list(map(int, input().split()))
copyL = list(filter(lambda element: element % 2 == 0, L))
[print(x, end=" ") for x in copyL]
