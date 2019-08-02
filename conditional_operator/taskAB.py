num_bar = int(input())
if num_bar // 10 == 1 or num_bar // 10 == 11:
    print(num_bar, "bochek")
else:
    if num_bar % 10 == 0 or (4 < num_bar % 10 <= 9):
        print(num_bar, "bochek")
    elif num_bar % 10 == 1:
        print(num_bar, "bochka")
    else:
        print(num_bar, "bochki")
