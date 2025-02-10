arr = [23,34,45,90,67,78,89,90,21,32]

def duplicate(arr1):
    for i in arr1:
        if arr1.count(i)>1:
            return True
    return False

res = duplicate(arr)
if res:
    print("Duplicate")
else:
    print("All unique")