week_name = input("Enter the week day: ").lower()
if week_name == 'sunday':
    print("Enter it's a holiday")
elif week_name == 'monday' or week_name == 'tuesday' or week_name == 'wednesday' or week_name == 'thursday' or week_name == 'friday' or week_name == 'saturday':
    print("It is a working day")
else:
    print("Invalid Input")