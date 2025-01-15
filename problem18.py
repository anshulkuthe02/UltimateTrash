data1 = {
    "name":"Joe Root",
    "address":"226, Blecker Street",
    "contactno":234-235-4567
}

print(data1["name"])
print(data1["address"])
data1["contactno"] = int(input("Enter new contac no: "))
print(f"The new ph no is: {data1["contactno"]}")