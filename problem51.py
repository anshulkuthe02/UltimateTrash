'''
from datetime import datetime

def days(start,end):
    start = datetime.strptime(start)
    end = datetime.strptime(end)
    diff = abs((end-start).days)
    print(f"The difference b/w entered days is {diff}")

date1 = input("Enter first date: ")
date2 = input("Enter end date: ")
days(date1,date2)
'''

from datetime import datetime

# Input: Get the two dates from the user
date1_str = input("Enter the first date (YYYY-MM-DD): ")
date2_str = input("Enter the second date (YYYY-MM-DD): ")

# Convert strings to datetime objects
date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# Calculate the difference between the dates
difference = abs((date2 - date1).days)

# Output the result
print(f"The number of days between {date1_str} and {date2_str} is {difference} day(s).")

