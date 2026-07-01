def login():
    username = "admin"
    password = "iusearchbtw"
    print("Welcome To Arch Linux")
    ask_username = input("Enter Your Username : ")
    if ask_username == username:
        print("Username Correct")
        ask_passwd = input("Enter Your Password :")
        if ask_passwd == password:
            print("Password Is Correct")
            print(f"Welcome {username}")
        else:
                print("Password Isn't Correct")
    else:
         print("Username Isn't Correct")

if __name__ == "__main__":
    login()


