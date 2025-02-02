from datetime import datetime
def date_n(reply):
    if reply == "yes":
        print(datetime.now())
    elif reply == "no":
        print("Have a good day")
    else:
        print("Check your spelling")

ans = input("Enter your reply: ").lower()
date_n(ans)