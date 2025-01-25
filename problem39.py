num = []; sum = 0; mul = 1
for i in range(5):
    a = int(input("Enter numbers: "))
    num.append(a)
    sum += num[i]
    mul *= sum
print(f"The final result is: {mul}")