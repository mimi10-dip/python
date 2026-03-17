#1
seconds = 42 * 60 + 42
print("1:", seconds, "seconds")
#2
miles = 10 / 1.61
print("2:", miles, "miles")
#3
total_seconds = 42 * 60 + 42
hours = total_seconds / 3600
distance_miles = 10 / 1.61
speed = distance_miles / hours
print("Speed:", speed, "miles/hour")
pace = total_seconds / distance_miles
minutes = int(pace // 60)
seconds = int(pace % 60)
print("Pace:", minutes, "minutes", seconds, "seconds per mile")
