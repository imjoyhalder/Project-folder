# Create a libaray
import collections
import datetime
l = ["Book1","Book2","Book3","Book4","Book5","Book6","Book7","Book8","Book9","Book10",
"Book11","Book12","Book13","Book14","Book15","Book16","Book18","Book19","Book20","Book21",
"Book22","Book23","Book24","Book25","Book26","Book27","Book28","Book29","Book30"
,"Book31","Book32","Book33","Book34","Book35","Book36","Book37","Book38","Book39","Book40"]
register = [{"Name":"Joy Halder","ide":101}]
lend_b = {}
detail_employ = {}
i = {}
class libaray:
    def __init__(self,book_list,libaray_name):
        self.book_list = book_list
        self.libaray_name = libaray_name
    def reg(self):
        Name = input("Enter your name: ")
        ide = int(input("You ide number: "))
        new = {"Name":"{Name}","ide":{ide}}
        #for i in register:
        if register[0] == new:
            print("You are already Registered in this libaray")

    def display(self):
        print("Book list")
        print()
        print(l)

    def lend(self):
        print("This is our book list")
        print(l,"\n")
        ask = input("What's book do you want\n")
        if ask in l:  
            name = input("Please Enter your name: ")
            detail_employ[f"{name}"]=[f"{ask}"]
            l.remove(f"{ask}")
            today = datetime.datetime.today()
            print(f"""On {today} you lend {ask} book From Education Libaray 
            and you must return it on {today+{datetime.timedelta(days=7)}}""")
            
        else: 
            print(f"Sorry {ask} Book is not aviable in this laibaray")
            
    def employ_data(self):
        pass







obj =libaray(l,"Education Libaray")

obj.lend()
obj.employ_data()