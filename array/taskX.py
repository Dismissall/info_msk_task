sizeL, steps = map(int, input().split())
L = ["I"] * sizeL

for i in range(steps):
    begin, end = map(int, input().split())
    for element in range(begin - 1, end):
        L[element] = '.'

[print(x, end="") for x in L]
