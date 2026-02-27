print("Your username should be 12 letter long. Should not contain any numbers and spaces.")
username = input("Enter your username: ")

if len(username) > 12:
    print("Username can't be more than 12 characters!")
elif not username.find(" ") == -1:
    print("Username can not contain spaces!")
elif not username.isalpha():
    print("Username can not contain ny numbers!")
else:
    print(f"Welcome {username}")