from collections import Counter

L = list(map(int, input().split()))
print(Counter(L).most_common(1)[0][0])
