def fact(num):
    if num == 1:
        return num
    else:
        return num*fact(num-1)    


num1 = int(input("Enter number: "))
fact(num1)
print(f"The factorial of {num1} is {fact(num1)}")