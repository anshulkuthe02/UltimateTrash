import math
num = int(input("Enter the angle: "))
code = input("Enter the code s for sin and c for cos: ")
if code == 's':
    code1 = math.sin(num)
    print(code1)
elif code == 'c':
    code1 = math.cos(num)
    print(code1)
else:
    print("Check the code correctly")
