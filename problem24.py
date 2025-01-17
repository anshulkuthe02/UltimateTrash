a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
oper = int(input("Enter operator: "))
if oper == 1:
    print(f"{a+b}")
elif oper == 2:
    print(f"{a-b}")
elif oper == 3:
    print(f"{a*b}")
elif oper == 4:
    print(f"{a//b}")
elif oper == 5:
    print(f"{a**b}")
else:
    print("Invalid Operator, check operator.")