import math
operator = input("Enter r for radians or d for degrees: ")
if operator == 'r':
    num = float(input("Enter degrees to convert in radians: "))
    print(f"The values in radian goes: {num*(math.pi/180)}")
elif operator == 'd':
    num = float(input("Enter radians to convert in degrees: "))
    print(f"The values in degree goes: {num*(180/math.pi)}")
else:
    print("Invalid operator! Check again")