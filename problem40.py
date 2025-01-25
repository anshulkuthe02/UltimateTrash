user = input("Enter username: ")
def username(u):
    if u.isalnum():
        print(f"Your username {str(u)} is correct")
    else:
        print("Not correct!")
username(user)