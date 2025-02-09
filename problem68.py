rolls = []
for i in range(6):
    ip = int(input("Enter rolls: "))
    rolls.append(ip)
rolls.sort(reverse=True)
print(rolls)

