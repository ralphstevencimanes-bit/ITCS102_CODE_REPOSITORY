from getpass import getpass

u ="steven"
p = "cimanes"

isLogin = False 

while isLogin == False:

    user = input("Enter Your Username ---> ")
    password = getpass("Enter Your Password ---> ")

    if user == u and password == p:
        print("Login Successfully")
        isLogin = True

    else:
        print("Login Failed")
        isLogin = False
