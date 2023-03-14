place = ["1.Barisal to Dhaka", "2.Barisal to Khulna", "3.Barisal to Rajsahi","4.Barisal to Gopalgonj","5.Barisal to Shylet","6.Barisal to Pabna "]
for i in place:
    print(i)
choice = int(input("Enter your choice: "))
name = input("Enter your name: ")
print(f"Welcome {name} this ticket counter")
if choice == 1:
    print(f"For every teckits cost 700 tk . {place[0]}")
    how = int(input("How many tickets do you want to buy: "))
    if how>53:
        print(f"Sorry {name} you can not buy 53 tickets at a time")
    else:
        print(f"You buy {how} tickets and total cost {how*700} tk")
        print("Thank you come again")

elif choice == 2:
    print(f"For every tickets cost 564 tk . {place[1]}")
    how = int(input("How many tickets do you want to buy: "))
    if how>53:
        print(f"Sorry {name} you can not buy 53 teckits at a time")
    else:
        print(f"You buy {how} tickets and total cost {how*564} tk")
        print("Thank you come again")

elif choice == 3:
    print(f"For every teckits cost 756 tk. {place[2]}")
    how = int(input("How many teckits do you want to buy: "))
    if how>53:
        print(f"Sorry {name} you can not buy 53 teckits at a time")
    else:
        print(f"You buy {how} tickets and total cost {how*756} tk")
        print("Thank you come again")

elif choice == 4:
    print(f"For every teckits cost 556 tk. {place[3]}")
    how = int(input("How many teckits do you want to buy: "))
    if how>53:
        print(f"Sorry {name} you can not buy 53 teckits at a time")
    else:
        print(f"You buy {how} tickets and total cost {how*556} tk")
        print("Thank you come again")

elif choice == 5:
    print(f"For every teckits cost 806 tk. {place[4]}")
    how = int(input("How many teckits do you want to buy: "))
    if how>53:
        print(f"Sorry {name} you can not buy 53 teckits at a time")
    else:
        print(f"You buy {how} tickets and total cost {how*806} tk")
        print("Thank you come again")
elif choice == 6:
    print(f"For every teckits cost 678 tk. {place[5]}")
    how = int(input("How many teckits do you want to buy: "))
    if how>53:
        print(f"Sorry {name} you can not buy 53 teckits at a time")
    else:
        print(f"You buy {how} tickets and total cost {how*678} tk")
        print(f"Thank you {name} come again")
else: 
    print("Please press right choice")