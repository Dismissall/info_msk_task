height = int(input())
up = int(input())
down = int(input())
print((-(height - up) % (up - down) + (height - up)) // (up - down) + 1)
