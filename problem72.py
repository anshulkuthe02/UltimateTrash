import random
code = []

for i in range(5):
    code.append(int(input("Enter the code: ")))
    
rand = random.choice(code)
print(rand)