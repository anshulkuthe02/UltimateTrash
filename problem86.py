chars = []
limit = int(input("Enter number of chars to input: "))

for i in range(limit):
    chars.append(input("Enter chars: "))

search = input("Enter element to search: ")
if search in chars:
    print("Yes")
else:
    print("No")
