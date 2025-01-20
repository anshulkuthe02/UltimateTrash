yr = int(input("Enter year: "))
if (yr%4==0 and yr%100!=0) or (yr%400==0):
    print(f"The {yr} is a leap year.")
else:
    print(f"The {yr} is not a leap year")
        