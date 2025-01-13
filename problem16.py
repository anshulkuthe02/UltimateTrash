##Compound operations on a number

num = int(input("Enter a number: "))

#sum
num += 5
print(num)

#difference
num -= 5
print(num)

#product
num *= 5
print(num)

#division
num /= 5
print(num)

#remainder
num %= 5
print(num)

#<= or >= or == operator
age = int(input("Enter age: "))

if age >= 18:
    print("The one can vote")
elif age < 18:
    print("The one is minor, cannot vote")
else:
    print("Invalid number or age")


