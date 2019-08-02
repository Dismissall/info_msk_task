c_rub = int(input())
c_penny = int(input())
p_rub = int(input())
p_penny = int(input())

c_penny += c_rub*100
p_penny += p_rub*100
print((p_penny - c_penny) // 100, (p_penny - c_penny) % 100)