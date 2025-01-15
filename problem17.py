chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p']
a = True
while a == True:
    for i in range(0,15):
        for j in range(i+1):
            print(chars[i], end=" ")
        print()

    for i in range(15,0,-1):
        for j in range(i):
            print(chars[i-1], end=" ")
        print()