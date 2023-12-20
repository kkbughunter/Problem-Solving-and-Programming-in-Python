from module import Authentication as auth

if __name__ == "__main__":
    userName = input("Enter your User Name: ")
    password = input("Enter your Password: ")
    auth.auth_user(userName, password)