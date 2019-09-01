L = list(map(int, input().split()))

element = input().split()
index = int(element[0])
value = int(element[1])
L.insert(index, value)

[print(element) for element in L]
