f_hour = int(input())
f_minute = int(input())
f_second = int(input())
s_hour = int(input())
s_minute = int(input())
s_second = int(input())

answer = (s_hour - f_hour) * 3600 + (s_minute - f_minute) * 60 + s_second - f_second
print(answer)
