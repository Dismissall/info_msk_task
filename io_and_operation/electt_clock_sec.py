spec_time = int(input())
seconds = spec_time % 60
minutes = spec_time // 60 % 60
hours = spec_time // 3600 % 24
print("{0}:{1:02d}:{2:02d}".format(hours, minutes, seconds))
