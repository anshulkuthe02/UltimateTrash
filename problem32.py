def max(num1,num2):
    if num1>num2:
        print(f"{num1} ia greater")
    elif num1<num2:
        print(f"{num2} is greater")
    else:
        print("The numbers are equal")

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
max(a,b)