data = [1,2.3,"ak","hello",56]

integer = 0
string = 0
floater = 0
for i in data:
    if(type(i) == int):
        integer += 1
    elif(type(i) == str):
        string += 1
    elif(type(i) == float):
        floater += 1
    else:
        print("Data type not defined")
print(integer)
print(string)
print(floater)