sec = int(input("Enter the amount of seconds: "))
hours = sec // 3600
r_seconds = sec % 3600
min = r_seconds // 60
seconds = r_seconds % 60

print(f"{sec} seconds = {hours} hours, {min} minutes, and {seconds} seconds.")
