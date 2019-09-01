L = list(map(int, input().split()))

index = int(input())
L.pop(index)

[print(element) for element in L]
