marks = 0; sum = 0
for i in range(1,7):
    marks = float(input(f"Enter marks of sub{i}: "))
    sum += marks

avg = sum/6
print(f"The sum is {sum} out of 600 and average is {avg}")
