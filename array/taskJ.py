L = list(map(int, input().split()))
new_height = int(input())
position = len([x for x, y in enumerate(L) if y >= new_height])
print(position + 1)
# position = len(list(filter(lambda heights: heights >= new_height, L)))
# print(position + 1)
