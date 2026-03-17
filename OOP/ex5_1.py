import time
total_seconds = time.time()
days = int(total_seconds // (24 * 3600))
remaining_seconds = int(total_seconds % (24 * 3600))
hours = remaining_seconds // 3600
minutes = (remaining_seconds % 3600) // 60
seconds = remaining_seconds % 60
print("Days since epoch:", days)
print("Current time:", hours, ":", minutes, ":", seconds)