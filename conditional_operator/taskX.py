num_cow = int(input())
if num_cow // 10 == 1:
    print(num_cow, "korov")
else:
    if num_cow % 10 == 0 or (4 < num_cow % 10 <= 9):
        print(num_cow, "korov")
    elif num_cow % 10 == 1:
        print(num_cow, "korova")
    else:
        print(num_cow, "korovy")