score = int(input("Enter score: "))
if score>= 95:
    print("The student gets A+ grade")
elif score >= 80:
    print("The student gets A grade")
elif score >= 70:
    print("The student gets B grade")
elif score >= 60:
    print("The student gets C grade")
elif score < 60:
    print("The student is failed.")