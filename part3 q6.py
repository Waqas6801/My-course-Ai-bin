minutes = int(input("Enter minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes is {hours} hours and {remaining_minutes} minutes")