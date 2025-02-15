num = []

for i in range(5):
    num.append(int(input("Enter numbers: ")))

ip = int(input("Enter number to be forked: "))
if ip < 5:
    print("Greater number: ",num[ip+1])
    print("Smaller number: ",num[ip-1])
elif ip == 5:
    print("Smaller number",num[ip-1])
elif ip == 0:
    print("Greater number: ",num[ip+1])
else:
    print("Invalid code")

print(num)