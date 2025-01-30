def hours_to_seconds(hours):
    return hours * 60 * 60

hours = float(input("Enter the number of hours: "))
seconds = hours_to_seconds(hours)
print(f"{hours} hour(s) is equal to {seconds} second(s).")
