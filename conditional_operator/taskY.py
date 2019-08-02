num_trip = int(input())
f_ticket = 0
s_ticket = 0

t_ticket = num_trip // 60
num_trip %= 60

if num_trip >= 35:
    t_ticket += 1
    num_trip = 0
elif num_trip >= 10:
    s_ticket = num_trip // 10
    num_trip = num_trip % 10
if num_trip == 9:
    s_ticket += 1
    num_trip = 0
if 0 < num_trip <= 8:
    f_ticket = num_trip
print(f_ticket, s_ticket, t_ticket)
