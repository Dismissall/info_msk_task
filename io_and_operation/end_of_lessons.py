les_count = int(input())
even_less = (les_count - 1) // 2
odd_less = les_count - even_less - 1
minutes = 45 * les_count + 5 * (3 * even_less + odd_less)
hours = 9 + minutes // 60
minutes = minutes % 60
print(hours, minutes)
