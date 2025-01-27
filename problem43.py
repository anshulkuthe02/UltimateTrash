start = int(input("Enter first input: "))
end = int(input("Enter last input: "))
ranged = end - start

for i in range(ranged):
    next_num =  start + i
    print(next_num)
print(end)