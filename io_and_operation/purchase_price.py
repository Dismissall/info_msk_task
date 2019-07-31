rub = int(input())
penny = int(input())
pie = int(input())

rub *=pie
penny *= pie
rub += penny // 100
penny = penny % 100
print(rub, penny)
