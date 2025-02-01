arr = [23,44,55,87,1,99,33,54,9,21]
target = int(input("enter number: "))
i = 0
while i < len(arr) and arr[i] != target:
    i += 1
print(i if i < len(arr) else "not found")