def scholar():
    score = []
    sum = 0; all = 0
    print("Enter marks here(out of 100):")
    for i in range(10):
        marks = int(input(""))
        score.append(marks)
        sum += marks
    print(sum)

    if sum == 1000:
        print("Total scholarship. FREE EDUCATION")
    elif sum < 1000:
        print("80% Monthly fees deduction")
    elif sum < 800:
        print("60% Monthly fees deduction")
    elif sum < 600:
        print("50% Monthly fees deduction")
    elif sum < 500:
        print("No scholarships")
    else:
        print("Invalid score")
        
scholar()   