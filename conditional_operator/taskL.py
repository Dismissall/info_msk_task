length = int(input())
width = int(input())
piece = int(input())

if (piece % length == 0 or piece % width == 0) and piece < length*width:
    print("YES")
else:
    print("NO")
