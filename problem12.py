i = int(input("Enter pyramid length: "))

for k in range(i+1):
    for j in range(k):
        print("*", end=" ")
    print()
