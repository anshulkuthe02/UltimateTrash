def geometry(length):
    code = input("Enter A for area or P for perimeter: ")
    if code == 'A' or code == 'a':
        print(f"Area is: {length**2} cm.squ/m.squ")
    elif code == 'P' or code == 'p':
        print(f"Perimeter is: {4*length} cm/m")
    else:
        print("Check code!")

leng = float(input("Enter the length of square: "))
geometry(leng)