num_trip = int(input())
ticket_1 = 0
ticket_2 = 0
ticket_3 = 0
ticket_4 = 0
ticket_5 = num_trip // 60
num_trip %= 60

if num_trip >= 36:
    ticket_5 += 1
    num_trip = 0
elif num_trip >= 20:
    ticket_4 = num_trip // 20
    num_trip = num_trip % 20
if num_trip > 17:
    ticket_4 += 1
    num_trip = 0
elif num_trip >= 10:
    ticket_3 = num_trip // 10
    num_trip = num_trip % 10
if num_trip == 9:
    ticket_3 += 1
    num_trip = 0
elif num_trip >= 5:
    ticket_2 = num_trip // 5
    num_trip = num_trip % 5
if 0 < num_trip < 5:
    ticket_1 = num_trip
print(ticket_1, ticket_2, ticket_3, ticket_4, ticket_5)
