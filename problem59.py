def bio():
    ip = input("Enter the bio: ")
    print(f"The character count in bio is: {len(ip)}")
    print(f"The word count is: {len(ip.split())}")

bio()