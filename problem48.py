import random
def nums(num1,num2,c):
    c = num1
    num1 =num2
    num2 = c
    print(f"{num1} \t {num2}")
    
ca = 0
i1 = int(input("Enter num1: "))
i2 = int(input("Enter num2: "))
nums(i1,i2,ca)