number = []

for i in range(5):
    number.append(int(input("Enter numbers: ")))

if number[0] == number[-1]:
    print("First and last are same.")
else:
    print(number)