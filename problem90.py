students = []
for i in range(10):
    students.append(int(input("Enter age: ")))
print(students)

for i in students:
    if(i>14 and i<20):
        print(i)