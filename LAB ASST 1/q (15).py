
drop_per_sec = 1
seconds_in_day = 24 * 60 * 60  # 86400
days = int(input("Enter the no. of days: "))

total_drops = drop_per_sec * seconds_in_day * days
waste = total_drops / 8000  # 800 drops = 100ml

print(f"The liter count of water wasted in {days} days is: {waste:} liters")
