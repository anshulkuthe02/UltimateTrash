arr = []; tot = 0
name = input("Enter username: ")
for i in range(5):
    mks = int(input("Enter number: "))
    arr.append(mks)
    tot += mks
print(f"Hi {name}!")
print(f"The total is {mks}")
print(f"English: {arr[0]}")
print(f"AI: {arr[1]}")
print(f"Physics: {arr[2]}")
print(f"Computer: {arr[3]}")
print(f"Math: {arr[4]}")
