num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
oper = int(input("enter the number for the operation to be performed: "))

'''
1 -> Addition
2 -> subtraction
3 -> multiplication
4 -> division
5 -> remainder  '''

if oper == 1:
    res = num1 + num2
    print(f"The sum is: {res}")
elif oper == 2:
    res = num1 - num2
    print(f"The difference is: {res}")
elif oper == 3:
    res = num1 * num2
    print(f"The product is: {res}")
elif oper == 4:
    res = num1 / num2
    print(f"The result is: {res}")
elif oper == 5:
    res = num1 % num2
    print(f"The remainder obtained is: {res}")