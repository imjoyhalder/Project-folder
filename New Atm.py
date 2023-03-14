import time
print("Please Enter your card\n")
print("Loading................................")
time.sleep(2)
pin = 1234
balance = 4000
u_pin = int(input("Enter you 4 digits PIN: "))
count = 0
while True:
    if pin == u_pin:
        print("""
        0.Chacke Balance
        1.Withdraw 
        2.Deposit
        3.Exist
        """)
        count += 1
        choice = int(input("Enter your choice : "))
        if choice == int(0):
            print(f"Your current balance is {balance} tk\n")
        if choice == int(1):
            amount = int(input("Enter amount: "))
            if balance >= amount:
                calculate = balance - amount
                print(f"{amount} tk withdraw successful")
                print(f"Now your accout balance is {calculate}","\n")
               
            else:
                print("Insufficient Balance")
        if choice == int(2):
            agree = input("If you want to deposit enter Y/N: ")
            if agree == "Y":
                amount = int(input("How much money do want to deposit: "))
                total_tk = balance + amount
                print(f"{amount} tk withdraw successful")
                print(f"Now your accout balance is {total_tk}")
                
        if choice == int(3):
            print("Exist")
            break

        
    else:
        print("Invalid PIN")
        break