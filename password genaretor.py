# How to store data into a file

agree = input("Do you want to open an account here: ").lower()

def view():
    with open("clinte.txt","w") as file:
        file.write(f"Client Name: {name} ,Password: {password}")


def password():
    if password ()== 0:
        print("Nothing is not all in this time we need sometime to recover it okay")
def show_data():
    with open("clinte.txt","r") as file1:
        print(file1.read())


if agree == "yes" or " Yes" or "YES":
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    
else:  
    show_data()
