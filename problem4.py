age = int(input("Enter age: "))
rem = 18 - age
if age < 18:
    print(f"Sorry you're {age} that is below 18 so you can't participate. You can vote after {rem} years")
else:
    print("You're eligible to participate")