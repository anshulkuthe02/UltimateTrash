list1 = [100,199,23,24,25,27,34,57,78,89,90,99]
x = list1[0]
for i in range(len(list1)):
    if list1[i]>x:
        x = list1[i]
print(f"Largest element is: {x}")


