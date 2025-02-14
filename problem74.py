list1 = []

for i in range(5):
    list1.append(int(input("Enter marks")))
    list1.sort(reverse=True)
print(list1[1])