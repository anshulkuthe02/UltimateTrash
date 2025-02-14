color = []

for i in range(10):
    color.append(input(f"Enter color {i}: "))

new_list = color.copy()
new_list.pop()
print(f"Copied list = {new_list}")