L = list(map(int, input().split()))

max_val, min_val = max(L), min(L)
max_val_index, min_val_index = L.index(max_val), L.index(min_val)
L[min_val_index], L[max_val_index] = max_val, min_val

[print(element) for element in L]

