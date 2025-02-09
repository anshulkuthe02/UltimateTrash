num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if (num1 > 0 and num2 > 0) and (num1 < 50 and num2 < 50):
   print(f"The sum is : {num1+num2}")
else:
   print("Number out of bounds")
