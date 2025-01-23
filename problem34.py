lst1 = []
for i in range(5):
    a = input("Enter color: ")
    lst1.append(a)
    lst1.sort()
lst1.pop()
print(lst1)
