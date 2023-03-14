password = input("Enter your Password: ")
if len(password)>8:
    if password == password.isalpha:
        if password == password[:len(password)].islower:
            if password.isdigit() == 2 or 3:
                pass
            else:
                print("""
                This password so easy
                Pleas set a passord with Spicial Charecter numbers and Chapital letter""")
        else:
            pass
    else:
        print("""
                It is an Easy Password
                Pleas set a passord with Spicial Charecter numbers and Chapital letter""")
else:
    print("Set Password gretar than 8 character") 