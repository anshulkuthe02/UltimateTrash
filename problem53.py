from datetime import datetime
from datetime import date

'''
def convert(year):
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    today = date.today()
    diff = abs((today - date1).days)
    tot = diff * 24 * 60 * 60
    print(f"The total seconds one lived is: {tot}")

'''



age = int(input("Enter your age in years: "))
seconds_per_year = 365 * 24 * 60 * 60  # Days * Hours * Minutes * Seconds
leap_years = age // 4  # Approximate number of leap years in the age
total_seconds = (age * seconds_per_year) + (leap_years * 24 * 60 * 60)
print(f"You have lived approximately {total_seconds:,} seconds.")
