def percal():
    sum = 0
    total = int(input("Enter total: "))
    for i in range(digit):
        nums = int(input("Enter the numbers: "))
        sum += nums
    print(f"The percentage is: {(sum*100)/total}.2f")

digit = int(input("Enter number of digits: "))
percal()
