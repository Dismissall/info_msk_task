deposit = int(input())
percent = int(input())
exp_deposit = int(input())
count_year = 0

while deposit < exp_deposit:
    profit = deposit * percent / 100
    deposit = round(profit + deposit, 2)
    count_year += 1
else:
    print(count_year)
