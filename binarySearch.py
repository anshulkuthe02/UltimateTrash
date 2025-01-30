def binary(list,low,high,target):
    while low <= high:
        mid = (high+low)//2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid+1
        else:
            high = mid - 1
    return -1

arr = sorted([23,45,4,67,98,2,99,66])
print(arr)
result = binary(arr,0,len(arr)-1,99)
print(f"the result is: {result}")
