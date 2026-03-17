import math
r = 5
volume = (4/3) * math.pi * r**3
print("Volume:", volume)
price = 24.95
discount = 0.4
discount_price = price * (1 - discount)
book_cost = discount_price * 60
shipping = 3 + (60 - 1) * 0.75
total = book_cost + shipping
print("Total cost:", total)
start_hour = 6
start_minute = 52
start_time = start_hour * 60 + start_minute
easy_pace = 8 + 15/60
tempo_pace = 7 + 12/60
run_time = easy_pace + 3 * tempo_pace + easy_pace
end_time = start_time + run_time
end_hour = int(end_time // 60)
end_minute = int(end_time % 60)
print("You get home at:", end_hour, ":", end_minute)