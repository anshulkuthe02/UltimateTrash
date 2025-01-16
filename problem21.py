import array as ar
arr = ar.array('i',[]); 


for i in range(5):
    u1 = int(input("Enter elements: "))
    arr.append(u1)
temp = arr[0]
for j in range(5):
    if(arr[j] > temp):
        temp = arr[j]
print(f"The max element is: {temp}")

