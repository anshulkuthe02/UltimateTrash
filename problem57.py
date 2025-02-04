def avg():
    sum = 0
    for i in range(digit):
        nums = int(input("Enter the numbers: "))
        sum += nums
    print(f"The percentage is: {(sum)/digit}")

digit = int(input("Enter number of digits: "))
avg()
