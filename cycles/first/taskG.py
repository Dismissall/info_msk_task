num_power = int(input())
# Наркоманский вариант
print("%.5f" % (4 * sum((1 / (2 * x + 1) if x % 2 == 0 else 1 / (2 * x + 1) * (-1) for x in range(num_power + 1)))))
